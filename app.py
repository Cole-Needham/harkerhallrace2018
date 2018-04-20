# /usr/bin/env python
# Download the twilio-python library from twilio.com/docs/libraries/python
from twilio.rest import Client

# Find these values at https://twilio.com/user/account
account_sid = "AC15b4f279248b559ac41e6e92f039ce30"
auth_token = "b546ebf94dd2010a5646c4a68aadeac5"

client = Client(account_sid, auth_token)

client.api.account.messages.create(
    to="+12369820317",
    from_="+16138016729",
    body="Hello there!")
