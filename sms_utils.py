import africastalking

# Initialize Africa's Talking
username = "sandbox"  
api_key = "[YOUR-API-KEY]"  
africastalking.initialize(username, api_key)

sms = africastalking.SMS

def send_sms(to, message):
    try:
        response = sms.send(message, [to])
        print("SMS sent:", response)
    except Exception as e:
        print("Error sending SMS:", e)
