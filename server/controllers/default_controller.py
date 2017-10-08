from flask import jsonify

msgs = []


def display(message):
    global msgs
    msgs.append(message)
    return None, 204


def messages():
    global msgs
    msg_jsn = jsonify(msgs)
    msgs = []
    return msg_jsn, 200
