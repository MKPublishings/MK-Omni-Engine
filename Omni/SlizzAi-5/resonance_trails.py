import tkinter as tk
import random


class ResonanceTrailHUD:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("🌠 Resonance Trails")
        self.root.geometry("800x600")
        self.canvas = tk.Canvas(self.root, bg="black")
        self.canvas.pack(fill="both", expand=True)
        self.glyph_resonance = {
            "GLYPH-TRUTH": 3,
            "GLYPH-ECHO": 5,
            "GLYPH-RENDER": 2
        }

    def draw_trails(self):
        for i, (glyph, depth) in enumerate(self.glyph_resonance.items()):
            x = 100 + (i * 200)
            for j in range(depth):
                offset = j * 10
                self.canvas.create_oval(x - offset, 300 - offset, x + offset, 300 + offset, outline="purple")
            self.canvas.create_text(x, 300, text=glyph, fill="white")

    def run(self):
        self.draw_trails()
        self.root.mainloop()


if __name__ == "__main__":
    hud = ResonanceTrailHUD()
    hud.run()
