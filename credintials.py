from twilio.rest import Client
account_sid = "ACa9b1a8f47563e651a27df1a07ee3693d"
auth_token = "676c2333a547a82de3d70dac610c3687"
client = Client(account_sid, auth_token)
def send_sms(to, message_body):
    try:
        message = client.messages.create(
            from_= 'whatsapp:+14155238886',
            body = message_body,
            to = f'whatsapp:{to}'
        )
        print("Message sent Successfully : ", message.sid)
    except Exception as e:
        print(e)