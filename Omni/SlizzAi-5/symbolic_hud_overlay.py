import tkinter as tk
from datetime import datetime
import json
import os


class SymbolicHUDOverlay:

    def __init__(self, archive_path="legacy_archive/glyph_history.json", log_path="ritual_logs/invocation_ledger.txt"):
        self.archive_path = archive_path
        self.log_path = log_path
        self.root = tk.Tk()
        self.root.title("🧿 Symbolic HUD Overlay")
        self.root.geometry("800x600")
        self.canvas = tk.Canvas(self.root, bg="black")
        self.canvas.pack(fill="both", expand=True)
        self.glyphs = {}

    def load_archive(self):
        if os.path.exists(self.archive_path):
            with open(self.archive_path, "r") as f:
                self.glyphs = json.load(f)

    def draw_glyph(self, glyph, x, y, pulse=1):
        color = "gold" if "ASCENDED" in glyph else "cyan"
        size = 20 + pulse * 5
        self.canvas.create_oval(x - size, y - size, x + size, y + size, fill=color)
        self.canvas.create_text(x, y, text=glyph, fill="white", font=("Helvetica", 10, "bold"))

    def animate_invocations(self):
        self.canvas.delete("all")
        if os.path.exists(self.log_path):
            with open(self.log_path, "r") as f:
                lines = f.readlines()
            for i, line in enumerate(lines[-10:]):
                _, _, glyph = line.partition("::")
                x = 100 + (i * 60)
                y = 300
                self.draw_glyph(glyph.strip(), x, y, pulse=i)
        self.root.after(2000, self.animate_invocations)

    def run(self):
        self.load_archive()
        self.animate_invocations()
        self.root.mainloop()


if __name__ == "__main__":
    hud = SymbolicHUDOverlay()
    hud.run()
