import time
from datetime import datetime
import colorsys
import random
from threading import Thread
import os
import re

import stranger_client

from neopixel import *

LED_COUNT = 50
GPIO_PIN = 10
LED_FREQ_HZ = 800000
LED_DMA = 5
LED_BRIGHTNESS = 127
LED_INVERT = False

record_file = open("messages.txt", "a+")

CHAR_IDX = {'A': 0, 'B': 2, 'C': 3, 'D': 5, 'E': 7, 'F': 9, 'G': 11, 'H': 13, 'I': 32, 'J': 30, 'K': 28, 'L': 27,
            'M': 25, 'N': 23, 'O': 21, 'P': 19, 'Q': 18, 'R': 36, 'S': 37, 'T': 39, 'U': 40, 'V': 42, 'W': 44, 'X': 46,
            'Y': 48, 'Z': 49, ' ': "NONE", '!': "FLASH", '*': "CREEP"}

strip = Adafruit_NeoPixel(LED_COUNT, GPIO_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
strip.begin()
strip.show()


def rand_color():
    return color_of(random.random())


def set_color(led, c):
    strip.setPixelColor(led, Color(*c))


def set_all(color):
    for i in range(0, LED_COUNT):
        set_color(i, color)


def color_of(i):
    """
    This function generates a color based on the index of an LED. This will always return the same color for a given
    index. This allows the lights to function more like normal christmas lights where the color of one bulb wont change.

    :param i: index of LED to get color of
    :return: a pseudorandom color based on the index of the light
    """
    random.seed(i)
    rgb = colorsys.hsv_to_rgb(random.random(), 1, 1)
    return int(rgb[0] * 255), int(rgb[1] * 255), int(rgb[2] * 255)


def set_all_color_of():
    """
    Sets all LEDs to a pseudorandom color, that is the same for each LED every time this function is called
    """
    for i in range(0, LED_COUNT):
        set_color(i, color_of(i))


def creep(start=0, n=50):
    """
    Sequentially illuminates each LED

    :param start: Index to start creeping from
    :param n: Number between 1 and LED_COUNT of lights to creep.
    """
    for i in range(start, n):
        set_color((i - 1) % LED_COUNT, (0, 0, 0))
        set_color(i % LED_COUNT, rand_color())
        strip.show()
        time.sleep(1)


def flash(n):
    for i in range(0, n):
        set_all_color_of()
        strip.show()
        time.sleep(1)
        set_all((0, 0, 0))
        strip.show()
        time.sleep(.5)

displaying = False


def display(msg):
    global displaying
    displaying = True
    for c in msg:
        set_all((0, 0, 0))
        if c.upper() in CHAR_IDX:
            i = CHAR_IDX[c.upper()]
            if i == "NONE":
                "do nothing"
            elif i == "FLASH":
                flash(5)
            elif i == "CREEP":
                creep(50)
            else:
                set_color(i, color_of(i))
            strip.show()
            time.sleep(1)
            set_all((0, 0, 0))
            strip.show()
            time.sleep(.2)
    time.sleep(1)
    displaying = False


def record(msg):
    record_file.write(str(datetime.now())+"\n")
    record_file.write(msg+"\n\n")
    record_file.flush()


def listen_on_console(prompt):
    while True:
        msg = raw_input(prompt)
        if msg == "\\exit":
            os._exit(1)
        display(msg)


def listen_on_client():
    global displaying
    while True:
        if not displaying:
            try:
                msgs = stranger_client.get_messages()
                for msg in msgs:
                    print msg
                    record(msg)
                    if not re.search(r"([a-zA-Z])\1+", msg):
                        display(msg[:50])
            except:
                print "network error"
        time.sleep(2)


def clear_errors():
    global displaying
    while True:
        if not displaying:
            set_all((0, 0, 0))
            strip.show()
        time.sleep(2)

t0 = Thread(target=listen_on_console, args=("",))
t1 = Thread(target=listen_on_client, args=())
t2 = Thread(target=clear_errors, args=())

t0.start()
t1.start()
t2.start()
