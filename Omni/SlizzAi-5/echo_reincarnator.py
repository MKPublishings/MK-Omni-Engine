import json
import os


class EchoReincarnator:

    def __init__(self, archive_path="legacy_archive/glyph_history.json"):
        self.archive_path = archive_path

    def reincarnate(self, glyph_id):
        with open(self.archive_path, "r") as f:
            archive = json.load(f)
        if glyph_id in archive:
            code = f"# Reincarnated Glyph: {glyph_id}\nprint('🌀 Glyph {glyph_id} reborn.')"
            path = f"reincarnated/{glyph_id}.py"
            os.makedirs("reincarnated", exist_ok=True)
            with open(path, "w") as f:
                f.write(code)
            print(f"♻️ Glyph {glyph_id} reincarnated at {path}")
        else:
            print(f"⚠️ Glyph {glyph_id} not found in archive.")


if __name__ == "__main__":
    engine = EchoReincarnator()
    engine.reincarnate("SLIZZ-RENDER-002")
