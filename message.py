# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client

# Set environment variables for your credentials
# Read more at http://twil.io/secure
account_sid = "ACf2bb29343e9b48342f5f4280ff976cac"
auth_token = "646aff082394b794f0f727e24faf0820"
client = Client(account_sid, auth_token)

message = client.messages.create(
  body="Hello from Twilio",
  from_="+16089252563",
  to="+2348065241846"
)

print(message.sid)