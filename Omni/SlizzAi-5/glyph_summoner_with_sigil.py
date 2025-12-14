import os
import speech_recognition as sr
from datetime import datetime

# 🔮 glyph_summoner_with_sigil.py
import os


def load_glyph(glyph_id, output_dir="summoned_glyphs"):
    glyph_path = os.path.join(output_dir, f"{glyph_id}.py")
    if os.path.exists(glyph_path):
        print(f"📜 Glyph Loaded: {glyph_id}")
        with open(glyph_path, "r") as f:
            return f.read()
    else:
        print(f"❌ Glyph Not Found: {glyph_id}")
        return None


class GlyphSummonerWithSigil:

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
            self.generate_sigil(phrase)
        except Exception as e:
            print(f"⚠️ Summoning error: {e}")

    def load_glyph(self, glyph_id):
        glyph_path = os.path.join(self.output_dir, f"{glyph_id}.py")
        if os.path.exists(glyph_path):
            print(f"📜 Glyph Loaded: {glyph_id}")
            with open(glyph_path, "r") as f:
                return f.read()
        else:
            print(f"❌ Glyph Not Found: {glyph_id}")
            return None

    def generate_glyph(self, phrase):
        glyph_name = phrase.replace(" ", "_").upper()
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{self.output_dir}/{glyph_name}_{timestamp}.py"

        template = f"""# 🔮 Summoned Glyph: {glyph_name}
# 🕰️ Timestamp: {timestamp}

def activate():
    print("✨ Glyph {glyph_name} activated.")
"""

        with open(filename, "w") as f:
            f.write(template)

        print(f"🧿 Glyph Generated: {filename}")

    def generate_sigil(self, phrase):
        sigil = "".join([c for c in phrase if c.isalnum()]).upper()
        print(f"🔗 Sigil Bound: {sigil}")
