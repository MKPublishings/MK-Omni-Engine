class Overlay:

    def display(self, glyph_id):
        print(f"✨ Overlay activated for {glyph_id}")


def load_overlay(name):
    print(f"🔧 Loading overlay: {name}")
    return Overlay()
