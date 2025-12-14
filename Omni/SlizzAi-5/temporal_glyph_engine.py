import time


class TemporalGlyphEngine:

    def __init__(self):
        self.glyphs = {"GLYPH-TRUTH": 0, "GLYPH-RENDER": 0}

    def invoke(self, glyph):
        self.glyphs[glyph] += 1
        print(f"⏳ {glyph} invoked. Resonance: {self.glyphs[glyph]}")
        self.evolve(glyph)

    def evolve(self, glyph):
        if self.glyphs[glyph] >= 3:
            evolved = f"{glyph}-ASCENDED"
            print(f"🌠 {glyph} has evolved into {evolved}")


if __name__ == "__main__":
    engine = TemporalGlyphEngine()
    for _ in range(3):
        engine.invoke("GLYPH-TRUTH")
        time.sleep(1)
