import tkinter as tk
import json
import os


class DragToReclaimHUD:

    def __init__(self, archive_path="legacy_archive/glyph_history.json"):
        self.archive_path = archive_path
        self.root = tk.Tk()
        self.root.title("🖱️ Drag-to-Reclaim Ritual")
        self.root.geometry("800x600")
        self.canvas = tk.Canvas(self.root, bg="black")
        self.canvas.pack(fill="both", expand=True)
        self.glyphs = {}
        self.dragged = None

    def load_archive(self):
        if os.path.exists(self.archive_path):
            with open(self.archive_path, "r") as f:
                self.glyphs = json.load(f)

    def draw_glyphs(self):
        for i, glyph in enumerate(self.glyphs.keys()):
            x, y = 100 + (i * 60), 100
            tag = f"glyph_{i}"
            self.canvas.create_oval(x - 20, y - 20, x + 20, y + 20, fill="gray", tags=tag)
            self.canvas.create_text(x, y, text=glyph, fill="white", tags=tag)
            self.canvas.tag_bind(tag, "<ButtonPress-1>", lambda e, g=glyph: self.start_drag(g))
            self.canvas.tag_bind(tag, "<ButtonRelease-1>", lambda e: self.drop_glyph())

    def start_drag(self, glyph):
        self.dragged = glyph
        print(f"🖱️ Dragging {glyph}...")

    def drop_glyph(self):
        if self.dragged:
            print(f"♻️ Reclaiming {self.dragged} from archive...")
            # Rebirth logic placeholder
            self.dragged = None

    def run(self):
        self.load_archive()
        self.draw_glyphs()
        self.root.mainloop()


if __name__ == "__main__":
    hud = DragToReclaimHUD()
    hud.run()
