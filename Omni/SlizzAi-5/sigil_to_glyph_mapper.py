import hashlib
import random


class SigilToGlyphMapper:

    def __init__(self, phrase):
        self.phrase = phrase
        self.hash = hashlib.sha256(phrase.encode()).hexdigest()

    def extract_traits(self):
        traits = {
            "intensity": int(self.hash[0:2], 16) % 10,  # affects loop depth or animation speed
            "color_code": self.hash[2:8],  # maps to visual or functional theme
            "angle_seed": int(self.hash[8:12], 16) % 360,  # influences logic branching
            "pulse_variance": int(self.hash[12:14], 16) % 5  # affects randomness or echo depth
        }
        return traits

    def generate_behavior(self):
        traits = self.extract_traits()
        print(f"🔮 Mapping traits from sigil:")
        for k, v in traits.items():
            print(f"  {k}: {v}")

        # Example: generate a glyph function based on traits
        code = f"""
# 🔮 Glyph Behavior from Sigil Mapping
# Phrase: "{self.phrase}"
# Traits: {traits}

def glyph_behavior():
    print("✨ Activating glyph with sigil traits...")
    for i in range({traits['intensity']}):
        print("🔁 Pulse", i + 1)
    if {traits['pulse_variance']} > 2:
        print("🌠 Echo surge detected!")
    else:
        print("🌙 Stable invocation.")

if __name__ == "__main__":
    glyph_behavior()
"""
        filename = f"mapped_glyphs/{self.phrase.replace(' ', '_').upper()}_mapped.py"
        os.makedirs("mapped_glyphs", exist_ok=True)
        with open(filename, "w") as f:
            f.write(code)
        print(f"🧿 Glyph behavior module saved at {filename}")


if __name__ == "__main__":
    phrase = input("🔮 Enter summoning phrase: ")
    mapper = SigilToGlyphMapper(phrase)
    mapper.generate_behavior()
