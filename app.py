from flask import Flask, Response
from twilio.twiml.voice_response import VoiceResponse

# Flask instance
app = Flask(__app__)

# Root route for browser testing
@app.route("/")
def home():
    return "AI Receptionist is running! Use /voice for Twilio."

# /voice route for Twilio POST requests
@app.route("/voice", methods=["POST"])
def voice():
    response = VoiceResponse()
    response.say(
        "Thank you for calling. How can I help you today?",
        voice="alice"
    )
    return Response(str(response), mimetype="text/xml")

# Only run the app directly for local testing
if __name__ == "__main__":
    app.run()

