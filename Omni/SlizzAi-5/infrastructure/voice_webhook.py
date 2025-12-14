from flask import Flask, request
from infrastructure.room_router import route_command
from infrastructure.voice_feedback import VoiceFeedback

app = Flask(__name__)
feedback = VoiceFeedback()


@app.route("/invoke", methods=["POST"])
def invoke_glyph():
    data = request.get_json()
    command = data.get("command", "")
    print(f"🗣️ Remote Invocation: {command}")
    route_command(command)
    feedback.play_feedback()
    return {"status": "invoked", "command": command}


if __name__ == "__main__":
    app.run(port=5051)
