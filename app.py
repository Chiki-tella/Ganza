# from flask import Flask, request

# app= Flask(__name__)

# #This is the endpoint Africa's Talking will call
# @app.route("/ussd", methods=['POST'])
# def ussd():
#     #ussd gateaway sends these parameters to your app
#     session_id = request.values.get("sessionId",None) #unique session for each interaction
#     service_code = request.values.get("serviceCode", None) #The USSD code dialed
#     phone_number = request.values.get("phoneNumber",None) #User's phone number
#     text = request.values.get("text","") #The chain of user inputs

#     #This is where the app sends back a response to the USSD gateaway
#     #If you send "CON", the USSD session continues (user can reply)
#     #If you send "END", the USSD session ends (user cannot reply)
#     if text == "":
#         response = "CON Welcome to GanzaTech"
#         response += "1. Login"
#         response += "2. Register"
#     elif text == "1":
#         response = "CON Enter your username"
#     elif text == "2":
#         response = "CON Enter your email address"
#     elif text.startswith("1 "):
#         username = text[2:]
#         response = f"END Hello {username}, you have successfully logged in."
#     elif text.startswith("2 "):
#         email = text[2:]
#         response = f"END Thank you for registering with {email}."
#     else:
#         response = "END Invalid option. Please try again."

#     return response

# if __name__ == "__main__":
#     app.run(debug=True, port=5000)  # Run the Flask app on port 5000


# from flask import Flask, request
# from database import init_db, insert_user, authenticate_user, insert_product, get_products

# app = Flask(__name__)
# init_db()

# @app.route("/ussd", methods=['POST'])
# def ussd():
#     session_id = request.values.get("sessionId", None)
#     service_code = request.values.get("serviceCode", None)
#     phone_number = request.values.get("phoneNumber", None)
#     text = request.values.get("text", "")

#     # Split the text into steps
#     user_response = text.split("*")

#     # ---------------- LANGUAGE SELECTION ----------------
#     if text == "":
#         response = "CON Murakaza neza / Welcome\n"
#         response += "1. Kinyarwanda\n"
#         response += "2. English"

#     # ---------------- MAIN MENU (based on language) ----------------
#     elif user_response[0] in ["1", "2"]:
#         lang = "kin" if user_response[0] == "1" else "eng"

#         if len(user_response) == 1:
#             if lang == "kin":
#                 response = "CON Hitamo:\n1. Injira\n2. Iyandikishe"
#             else:
#                 response = "CON Choose:\n1. Login\n2. Register"

#         # ---------------- LOGIN ----------------
#         elif user_response[1] == "1":
#             if len(user_response) == 2:
#                 response = "CON Enter username:" if lang == "eng" else "CON Andika izina ryawe:"
#             elif len(user_response) == 3:
#                 response = "CON Enter password:" if lang == "eng" else "CON Andika ijambo ry'ibanga:"
#             elif len(user_response) == 4:
#                 username = user_response[2]
#                 password = user_response[3]
#                 user = authenticate_user(username, password)
#                 if user:
#                     if lang == "eng":
#                         response = "CON Login successful!\n1. Buyer\n2. Seller"
#                     else:
#                         response = "CON Kwiyinjiza byagenze neza!\n1. Umuguzi\n2. Umucuruzi"
#                 else:
#                     response = "END Invalid credentials!" if lang == "eng" else "END Izina cyangwa ijambo ry'ibanga sibyo!"

#         # ---------------- REGISTER ----------------
#         elif user_response[1] == "2":
#             if len(user_response) == 2:
#                 response = "CON Enter full name:" if lang == "eng" else "CON Andika amazina yawe yose:"
#             elif len(user_response) == 3:
#                 response = "CON Enter email:" if lang == "eng" else "CON Andika email yawe:"
#             elif len(user_response) == 4:
#                 response = "CON Choose username:" if lang == "eng" else "CON Hitamo izina ukoresha:"
#             elif len(user_response) == 5:
#                 response = "CON Enter password:" if lang == "eng" else "CON Andika ijambo ry'ibanga:"
#             elif len(user_response) == 6:
#                 fullname = user_response[2]
#                 email = user_response[3]
#                 username = user_response[4]
#                 password = user_response[5]
#                 # Default role None for now
#                 insert_user(fullname, email, username, password, role=None)
#                 response = "END Registration complete!" if lang == "eng" else "END Kwiyandikisha byagenze neza!"

#     # ---------------- POST LOGIN OPTIONS ----------------
#     elif user_response[2] == "1" or user_response[2] == "2":
#         lang = "kin" if user_response[0] == "1" else "eng"
#         role = "buyer" if user_response[2] == "1" else "seller"

#         # Buyer options
#         if role == "buyer":
#             if len(user_response) == 3:
#                 response = "CON 1. View products" if lang == "eng" else "CON 1. Reba ibicuruzwa"
#             elif len(user_response) == 4 and user_response[3] == "1":
#                 products = get_products()
#                 if products:
#                     product_list = "\n".join([f"{p[0]} - {p[1]} RWF" for p in products])
#                     response = f"END Products:\n{product_list}"
#                 else:
#                     response = "END No products yet." if lang == "eng" else "END Nta bicuruzwa birashyirwa ku isoko."

#         # Seller options
#         elif role == "seller":
#             if len(user_response) == 3:
#                 response = "CON 1. Add product" if lang == "eng" else "CON 1. Shyiraho igicuruzwa"
#             elif len(user_response) == 4 and user_response[3] == "1":
#                 response = "CON Enter product name:" if lang == "eng" else "CON Andika izina ry'igicuruzwa:"
#             elif len(user_response) == 5:
#                 response = "CON Enter price:" if lang == "eng" else "CON Andika igiciro:"
#             elif len(user_response) == 6:
#                 product_name = user_response[4]
#                 price = float(user_response[5])
#                 # For demo: assume seller_id = 1
#                 insert_product(1, product_name, price)
#                 response = "END Product added!" if lang == "eng" else "END Igicuruzwa cyongewe!"

#     else:
#         response = "END Invalid option."

#     return response


# if __name__ == "__main__":
#     app.run(debug=True, port=5000)

from flask import Flask, request
from database import (
    init_db, insert_user, authenticate_user,
    insert_product, get_products,  # <-- added here
    insert_product_draft, get_latest_draft,
    complete_product, get_buyers
)
import africastalking

# ---------------- CONFIG ----------------
AT_USERNAME = "sandbox"   # Change to your production username later
AT_API_KEY = "atsk_ea471ac85fba6d6b999f336e24d1304ae8ee26a13ca33816b133a4a89d0a076056ebc9a5"  # Paste your Africa's Talking sandbox API key
africastalking.initialize(AT_USERNAME, AT_API_KEY)
sms = africastalking.SMS

app = Flask(__name__)
init_db()

# ---------------- SMS FUNCTION ----------------
def send_sms_to_buyers(message):
    buyers = get_buyers()
    phone_numbers = [b[0] for b in buyers]  # assuming get_buyers() returns [(phone,), (phone,), ...]
    if phone_numbers:
        try:
            response = sms.send(message, phone_numbers)
            print("SMS sent:", response)
        except Exception as e:
            print("SMS error:", e)


@app.route("/ussd", methods=['POST'])
def ussd():
    session_id = request.values.get("sessionId", None)
    service_code = request.values.get("serviceCode", None)
    phone_number = request.values.get("phoneNumber", None)
    text = request.values.get("text", "")

    user_response = text.split("*")

    # ---------------- LANGUAGE SELECTION ----------------
    if text == "":
        response = "CON Murakaza neza / Welcome\n"
        response += "1. Kinyarwanda\n"
        response += "2. English"

    # ---------------- MAIN MENU ----------------
    elif user_response[0] in ["1", "2"]:
        lang = "kin" if user_response[0] == "1" else "eng"

        if len(user_response) == 1:
            response = "CON 1. Login\n2. Register" if lang == "eng" else "CON 1. Injira\n2. Iyandikishe"

        # ---------------- LOGIN ----------------
        elif user_response[1] == "1":
            if len(user_response) == 2:
                response = "CON Enter username:" if lang == "eng" else "CON Andika izina:"
            elif len(user_response) == 3:
                response = "CON Enter password:" if lang == "eng" else "CON Andika ijambo ry'ibanga:"
            elif len(user_response) == 4:
                username = user_response[2]
                password = user_response[3]
                user = authenticate_user(username, password)
                if user:
                    response = "CON 1. Buyer\n2. Seller" if lang == "eng" else "CON 1. Umuguzi\n2. Umucuruzi"
                else:
                    response = "END Invalid login!" if lang == "eng" else "END Kwiyinjiza ntibikunze!"

        # ---------------- REGISTER ----------------
        elif user_response[1] == "2":
            if len(user_response) == 2:
                response = "CON Choose username:" if lang == "eng" else "CON Hitamo izina:"
            elif len(user_response) == 3:
                response = "CON Choose password:" if lang == "eng" else "CON Hitamo ijambo ry'ibanga:"
            elif len(user_response) == 4:
                username = user_response[2]
                password = user_response[3]
                insert_user(username=username, password=password, phone=phone_number, role=None)
                response = "END Registration complete!" if lang == "eng" else "END Kwiyandikisha byagenze neza!"

    # ---------------- POST LOGIN OPTIONS ----------------
    elif user_response[2] in ["1", "2"]:
        lang = "kin" if user_response[0] == "1" else "eng"
        role = "buyer" if user_response[2] == "1" else "seller"

        # ---------------- BUYER ----------------
        if role == "buyer":
            if len(user_response) == 3:
                response = "CON 1. View products" if lang == "eng" else "CON 1. Reba ibicuruzwa"
            elif len(user_response) == 4 and user_response[3] == "1":
                products = get_products()
                if products:
                    product_list = "\n".join([f"{p[0]} - {p[1]} RWF" for p in products])
                    response = f"END Products:\n{product_list}"
                else:
                    response = "END No products yet." if lang == "eng" else "END Nta bicuruzwa birahari."

        # ---------------- SELLER ----------------
        elif role == "seller":
            if len(user_response) == 3:
                response = "CON 1. Add product" if lang == "eng" else "CON 1. Shyiraho igicuruzwa"
            elif len(user_response) == 4 and user_response[3] == "1":
                response = "CON Enter product name:" if lang == "eng" else "CON Andika izina ry'igicuruzwa:"
            elif len(user_response) == 5:
                response = "CON Enter price:" if lang == "eng" else "CON Andika igiciro:"
            elif len(user_response) == 6:
                product_name = user_response[4]
                price = float(user_response[5])
                insert_product(1, product_name, price)  # seller_id = 1 (demo)
                
                # 🔹 Notify buyers via SMS
                message = f"New product added: {product_name} - {price} RWF"
                send_sms_to_buyers(message)

                response = "END Product added!" if lang == "eng" else "END Igicuruzwa cyongewe!"

    else:
        response = "END Invalid option."

    return response


if __name__ == "__main__":
    app.run(debug=True, port=5000)

