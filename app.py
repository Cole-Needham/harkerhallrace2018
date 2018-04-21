# /usr/bin/env python
# Download the twilio-python library from twilio.com/docs/libraries/python
import os
from twilio.rest import Client
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
from twilio import twiml

app = Flask(__name__)
account_sid = "AC15b4f279248b559ac41e6e92f039ce30"
auth_token = "b546ebf94dd2010a5646c4a68aadeac5"
t_client = Client(account_sid,auth_token)
@app.route("/sms/", methods=['GET', 'POST'])
def sms_echo():
    # https://github.com/twilio/twilio-python#api-credentials

    sms_body = request.args.get('Body')
    app.logger.info('body: `{}`'.format(sms_body))

    if sms_body is None:
        app.logger.warning('Null SMS body.')
        return 'Bad request from Twilio client.'
    else:
        return ('<?xml version="1.0" encoding="UTF-8" ?>'
                '<Response>'
                '<Message>{}</Message>'
                '</Response>'.format(sms_body))
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int('5000'))

else:
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)
    app.logger.addHandler(stream_handler)
