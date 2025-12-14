import speech_recognition as sr
import os
from datetime import datetime


class GlyphSummoner:

    def __init__(self, output_dir="summoned_glyphs"):
        self.recognizer = sr.Recognizer()
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

    def listen_and_summon(self):
        with sr.Microphone() as source:
            print("🔮 Speak your glyph summoning phrase...")
            audio = self.recognizer.listen(source)

        try:
            phrase = self.recognizer.recognize_google(audio).lower()
            print(f"🗣️ Heard: {phrase}")
            self.generate_glyph(phrase)
        except Exception as e:
            print(f"⚠️ Summoning error: {e}")

    def generate_glyph(self, phrase):
        glyph_name = phrase.replace(" ", "_").upper()
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{self.output_dir}/{glyph_name}_{timestamp}.py"

        template = f"""# 🔮 Summoned Glyph: {glyph_name}
# Phrase: "{phrase}"
# Timestamp: {timestamp}

def {glyph_name.lower()}():
    print("✨ Glyph '{glyph_name}' activated via summoning phrase: '{phrase}'")

if __name__ == "__main__":
    {glyph_name.lower()}()
"""
        with open(filename, "w") as f:
            f.write(template)
        print(f"🧿 Glyph '{glyph_name}' summoned at {filename}")


if __name__ == "__main__":
    summoner = GlyphSummoner()
    summoner.listen_and_summon()
