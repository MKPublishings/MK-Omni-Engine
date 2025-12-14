import json
import os
from PIL import Image, ImageDraw


class SigilEvolutionEngine:

    def __init__(self, log_path="ritual_logs/invocation_ledger.txt", archive_dir="sigil_archive"):
        self.log_path = log_path
        self.archive_dir = archive_dir
        os.makedirs(self.archive_dir, exist_ok=True)
        self.invocation_counts = {}

    def track_invocations(self):
        if not os.path.exists(self.log_path):
            return
        with open(self.log_path, "r") as f:
            lines = f.readlines()
        for line in lines:
            _, _, glyph = line.partition("::")
            glyph = glyph.strip()
            self.invocation_counts[glyph] = self.invocation_counts.get(glyph, 0) + 1

    def evolve_sigil(self, glyph):
        count = self.invocation_counts.get(glyph, 1)
        size = 100 + count * 10
        img = Image.new("RGB", (size, size), "black")
        draw = ImageDraw.Draw(img)

        for i in range(count):
            radius = 10 + i * 5
            color = (255 - i * 10, 100 + i * 5, 200)
            draw.ellipse(
                [(size // 2 - radius, size // 2 - radius), (size // 2 + radius, size // 2 + radius)],
                outline=color
            )

        draw.text((10, size - 20), f"{glyph} x{count}", fill="white")
        filename = f"{self.archive_dir}/{glyph}_evolved.png"
        img.save(filename)
        print(f"🌠 Evolved sigil saved: {filename}")

    def run(self):
        self.track_invocations()
        for glyph in self.invocation_counts:
            self.evolve_sigil(glyph)


if __name__ == "__main__":
    engine = SigilEvolutionEngine()
    engine.run()
