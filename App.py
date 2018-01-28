from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse, Message
from twilio.rest import Client
import urllib

account_sid = "ACbc21a369eb35233ebe1a8995310c634b"
auth_token = "9ba041095cfac3649aad180dd7f78d52"

client = Client(account_sid, auth_token)
app = Flask(__name__)

list_of_responses = {}
@app.route('/sms', methods=['GET','POST'])
def inbound_sms():
    message = urllib.parse.unquote(request.form['Body'])
    if(message == 'Yes'):
        list_of_responses[request.form['From']] += 1
    elif(message == 'No'):
        response = MessagingResponse()
        response.message("Thank you for your response", "12142264980")
    else:
        response = MessagingResponse()
        response.message("Please Respond Yes or No")
    return message

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
