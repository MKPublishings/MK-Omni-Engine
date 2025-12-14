from flask import Flask, jsonify
from assets.overlays.sigil_dashboard import SigilDashboard

app = Flask(__name__)
dashboard = SigilDashboard()


@app.route("/sigils", methods=["GET"])
def get_sigils():
    return jsonify(dashboard.ui.state)


@app.route("/sigils/<room>", methods=["GET"])
def get_room_sigil(room):
    sigil = dashboard.ui.state.get(room, {})
    return jsonify(sigil)


if __name__ == "__main__":
    dashboard.update_room("renderer", "SLIZZ-RENDER-002", "active")
    dashboard.update_room("logic", "GLYPH-TRUTH", "invoked")
    app.run(port=5050)
