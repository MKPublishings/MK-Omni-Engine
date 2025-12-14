import json
from collections import Counter


class GlyphAnalytics:

    def __init__(self, log_path="legacy_archive/echo_logs.md"):
        self.log_path = log_path

    def analyze(self):
        with open(self.log_path, "r") as f:
            lines = f.readlines()
        glyphs = [line.split()[1] for line in lines if "Glyph" in line]
        stats = Counter(glyphs)
        print("📊 Glyph Invocation Stats:")
        for glyph, count in stats.items():
            print(f"🔹 {glyph}: {count} invocations")


# Example usage
if __name__ == "__main__":
    analytics = GlyphAnalytics()
    analytics.analyze()
