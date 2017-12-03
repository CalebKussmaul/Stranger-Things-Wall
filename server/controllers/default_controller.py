from flask import jsonify, render_template
from settings import settings

msgs = []


def index():
    return render_template('index.html')


def display(message):
    global msgs
    msgs.append(message)
    print(message)
    return None, 204


def messages(password):
    if password == settings.password:
        global msgs
        msg_jsn = jsonify(msgs)
        msgs = []
        return msg_jsn, 200
