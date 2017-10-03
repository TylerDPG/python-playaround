from twilio import rest
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC185b772ae5fb4dbd3cd8c8dce64e7dd7"
auth_token  = "5c73b3d658ee648a6cc4d499a3c5c125"
client = rest.TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(body="Hi my name is Slim Shady.",
    to="+18565202619",    # Replace with your phone number
    from_="+18563228374") # Replace with your Twilio number
print message.sid
