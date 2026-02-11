import africastalking

# Initialize Africa's Talking
username = "sandbox"  
api_key = " atsk_ea471ac85fba6d6b999f336e24d1304ae8ee26a13ca33816b133a4a89d0a076056ebc9a5"  
africastalking.initialize(username, api_key)

sms = africastalking.SMS

def send_sms(to, message):
    try:
        response = sms.send(message, [to])
        print("SMS sent:", response)
    except Exception as e:
        print("Error sending SMS:", e)
