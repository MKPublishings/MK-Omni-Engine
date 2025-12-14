import speech_recognition as sr
import json
import os


class VoiceReincarnator:

    def __init__(self, archive_path="legacy_archive/glyph_history.json"):
        self.recognizer = sr.Recognizer()
        self.archive_path = archive_path

    def listen_and_rebirth(self):
        with sr.Microphone() as source:
            print("🎤 Speak glyph ID to reincarnate...")
            audio = self.recognizer.listen(source)

        try:
            spoken = self.recognizer.recognize_google(audio).upper()
            print(f"🔊 Heard: {spoken}")
            self.rebirth(spoken)
        except sr.UnknownValueError:
            print("⚠️ Could not understand the glyph ID.")
        except sr.RequestError as e:
            print(f"⚠️ Error: {e}")

    def rebirth(self, glyph_id):
        with open(self.archive_path, "r") as f:
            archive = json.load(f)
        if glyph_id in archive:
            code = f"# Reborn Glyph: {glyph_id}\nprint('♻️ {glyph_id} reborn.')"
            path = f"reincarnated/{glyph_id}.py"
            os.makedirs("reincarnated", exist_ok=True)
            with open(path, "w") as f:
                f.write(code)
            print(f"🧬 {glyph_id} reincarnated at {path}")
        else:
            print(f"❌ Glyph {glyph_id} not found in archive.")


if __name__ == "__main__":
    vr = VoiceReincarnator()
    vr.listen_and_rebirth()
