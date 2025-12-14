from infrastructure.voice_listener import listen_for_glyph
from infrastructure.room_router import route_command
from invocation_ledger import InvocationLedger
from infrastructure.voice_feedback import VoiceFeedback


class AIFamiliar:

    def __init__(self):
        self.ledger = InvocationLedger()
        self.feedback = VoiceFeedback()

    def awaken(self):
        print("🧬 AI Familiar Awakened. Listening for glyphs...")
        while True:
            phrase = listen_for_glyph()
            if phrase == "exit":
                print("🛑 Familiar Resting.")
                break
            route_command(phrase)
            self.ledger.record(f"VOICE:{phrase}", "invoked")
            self.feedback.play_feedback()


if __name__ == "__main__":
    familiar = AIFamiliar()
    familiar.awaken()
