# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 13:41:09 2016

@author: marco
"""

import wikipedia
from flask import Flask, request
from twilio.rest import TwilioRestClient
import twilio.twiml
app = Flask(__name__)
account = "ACc6c3f07559484efcb7ca167ecd0c1209"
token = "bbe3fc010c1b94ccce6f0566ec36095f"
@app.route('/')
def index():
    client = TwilioRestClient(account, token)
    client.messages.create(to="+447871218445",from_="+441461211007",body="Hello there!")
    return "Hello"
@app.route('/text', methods=['POST'])
def textReceived():
    text = wikipedia.summary(request.form.get('Body'), chars=1200)
    r = twilio.twiml.Response()
    r.message(text);
    #print(len(text), request.form.get('From'))
    #client = TwilioRestClient(account, token)
    #client.messages.create(to=request.form.get('From'),from_="+441461211007",body=text)
    return str(r)
if __name__ == '__main__':
    app.run(debug=True)