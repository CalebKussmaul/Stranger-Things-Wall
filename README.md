# Raspberry Pi Stranger Things Wall

This is set up to get around university wifi restrictions by hosting the server separately. 

**If you want to run everything on the Pi, [use this repo instead](https://github.com/CalebKussmaul/Stranger-Things-Integrated)**

#### In this GIT repo 

* **/website**: (optional) A simple HTML page with a form to send messages to the server
* **/server**: A flask server to recieve and hold messages, also includes the functionally of /website so you can just point your domain to this
* **/client**: A raspberry pi client to periodically poll the server for messages and display them on your wall

#### You will need

1. A second computer on a network that allows incoming traffic with python 2 installed
2. Raspberry pi - any model should work, I'm using a B+
3. [Wifi dongle](https://www.amazon.com/gp/product/B003MTTJOY) if model does not have wifi chip
5. [5v Power supply](https://www.amazon.com/gp/product/B00MHV7576/) DO NOT POWER LEDs DIRECTLY FROM PI GPIO. CONNECT THEM BOTH TO THE POWER SUPPLY.
6. Breadboard and jumper wires 
7. [Level shifter](https://www.amazon.com/gp/product/B00XW2L39K/) (Reccomended)
8. [WS2811 LEDs](https://www.amazon.com/gp/product/B01AG923GI/)
9. 3' x 4' posterboard, paint, command strips, clear tape

#### Server setup

1. Open terminal
2. Enter "git clone 'https://github.com/CalebKussmaul/Stranger-Things-Wall.git'"
3. Enter "cd Stranger-Things-Wall"
4. Enter "pip2 install -r server/requirements.txt"
5. Enter password and server IP into settings/settings.py
6. Enter "python2 -m server" to start the server

#### Client (raspberry pi part) setup

1. String wires on posterboard and paint letters corresponding to LEDs. There are 50 lights and 26 letters, so you will have to be somewhat creative. Use clear tape to point the LEDs to the letters
2. Install raspbian on pi
3. Connect pi and ws2811 LED strip to external 5v power source in parallel (see wiring below)
4. Connect LED data wire to the pi [GPIO 10](https://www.raspberrypi-spy.co.uk/wp-content/uploads/2012/06/Raspberry-Pi-GPIO-Layout-Model-B-Plus-rotated-2700x900.png) (actual pin number 19, I know it's confusing)
5. Install [rpi_ws281x library](https://github.com/jgarff/rpi_ws281x) (remember to disable sound card)
6. Open terminal
7. Enter "git clone 'https://github.com/CalebKussmaul/Stranger-Things-Wall.git'"
8. Enter "cd Stranger-Things-Wall/client"
9. Enter "pip2 install -r client/requirements.txt"
10. Copy settings.py from server, and in stranger.py and adjust character mapping to LEDs as necessary
11. Enter "python2 -m client" to start the client


#### Static webhost workaround

There is also an option to host the web form as a 3rd part. You might use this if you have a webhost that only allows static content, and you don't want to point your domain directly at your home IP. You will still need to have the server running elsewhere, and point the form action to that address. 

If you do not need this, simply point your domain to the server and the form will be accessible via http://yourdomain.com:8080/stranger. You may also want to change the port number in app.py to 80 instead of 8080. (this is not default since some consumer operating systems do not allow you to bind to that port). 

You should now be up and running. Test it by entering a message in the terminal, or over the web by going to http://\[your pi's IP address\]:8080/stranger/

If you want to allow messages from the external internet, you will need to use your router port-forward incoming traffic to your external IP to the pi's internal IP.

Note: technically the data wire takes 5v data, and the pi GPIO outputs on 3.3v. You may need to use [a level shifter](https://www.amazon.com/gp/product/B00XW2L39K/ref=oh_aui_detailpage_o00_s00?ie=UTF8&psc=1) however it works fine without it for me.

#### Wiring:

![Wiring](wall%20with%20level%20shifter.png)

but you can probably get away with this:

![Wiring without level shifter](wall%20without%20level%20shifter.png)