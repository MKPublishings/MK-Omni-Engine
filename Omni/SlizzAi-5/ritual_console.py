import speech_recognition as sr
import time


class RitualConsole:

    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.glyph_registry = {
            "invoke truth": "GLYPH-TRUTH",
            "reclaim echo": "GLYPH-ECHO",
            "ascend render": "GLYPH-RENDER-ASCENDED"
        }

    def listen_and_invoke(self):
        with sr.Microphone() as source:
            print("🎙️ Ritual Console activated. Speak your glyph...")
            audio = self.recognizer.listen(source)

        try:
            command = self.recognizer.recognize_google(audio).lower()
            print(f"🔊 Heard: {command}")
            if command in self.glyph_registry:
                glyph = self.glyph_registry[command]
                self.activate_glyph(glyph)
            else:
                print("❓ Unknown invocation. No glyph matched.")
        except sr.UnknownValueError:
            print("⚠️ Could not understand the invocation.")
        except sr.RequestError as e:
            print(f"⚠️ Invocation error: {e}")

    def activate_glyph(self, glyph):
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        print(f"🧿 {glyph} activated at {timestamp}")
        with open("ritual_logs/invocation_ledger.txt", "a") as f:
            f.write(f"{timestamp} :: {glyph} activated\n")


if __name__ == "__main__":
    console = RitualConsole()
    console.listen_and_invoke()
