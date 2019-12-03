from flask import Flask, request, render_template
from twilio import twiml 
from twilio.twiml.messaging_response import MessagingResponse
app = Flask(__name__)

@app.route("/")
def form():
    return render_template('form.html')

@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    body = request.values.get('Body', None)
    resp = MessagingResponse()

    body = str(body)
    try:
        body = body.encode("ASCII")
        body = body.decode("ASCII")
        resp.message(body)
        pass
    except :
        body = str("GOOD JOB BUUDDY YOU BROKE IT")
        resp.message(body)
        pass

    return str(resp)
if __name__ == "__main__":
    app.run(debug=True)