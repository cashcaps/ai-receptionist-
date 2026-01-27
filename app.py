from flask import Flask, Response
from twilio.twiml.voice_response import VoiceResponse

app = Flask(__name__)

@app.route("/voice", methods=["POST"])
def voice():
    response = VoiceResponse()
    response.say(
        "Thank you for calling. How can I help you today?",
        voice="alice"
    )
    return Response(str(response), mimetype="text/xml")

if __name__ == "__main__":
    app.run()
