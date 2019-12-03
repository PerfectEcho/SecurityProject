from flask import Flask, request, render_template
from twilio import twiml 
from twilio.twiml.messaging_response import MessagingResponse
app = Flask(__name__)

@app.route("/")
def form():
    return render_template('form.html')
@app.route("/EVERYTHINGISONFIRE")
def formTWO():
    return render_template('formTWO.html')
@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    body = request.values.get('Body', None)
    resp = MessagingResponse()

    body = str(body)
    try:
        body = body.encode("ASCII")
        body = body.decode("ASCII")
        resp.message("THIS TEXT DID NOTHING TRY AGAIN: " + body + '\n' + "http://1111a976.ngrok.io/")
        return str(resp)
        pass
    except :
        body = str("LOOK WHAT YOU DID..." + '\n' + "http://1111a976.ngrok.io/EVERYTHINGISONFIRE")
        resp.message(body)
        return str(resp)
        pass


if __name__ == "__main__":
    app.run(debug=True)