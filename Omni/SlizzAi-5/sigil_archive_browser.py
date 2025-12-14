import tkinter as tk
import os
from PIL import Image, ImageTk


class SigilArchiveBrowser:

    def __init__(self, archive_dir="sigil_archive"):
        self.archive_dir = archive_dir
        os.makedirs(self.archive_dir, exist_ok=True)
        self.root = tk.Tk()
        self.root.title("🗂️ Sigil Archive Browser")
        self.root.geometry("800x600")
        self.canvas = tk.Canvas(self.root, bg="black")
        self.canvas.pack(fill="both", expand=True)
        self.sigil_files = []

    def load_sigils(self):
        self.sigil_files = [f for f in os.listdir(self.archive_dir) if f.endswith(".png")]

    def display_sigils(self):
        self.canvas.delete("all")
        for i, file in enumerate(self.sigil_files):
            path = os.path.join(self.archive_dir, file)
            img = Image.open(path).resize((100, 100))
            photo = ImageTk.PhotoImage(img)
            x, y = 120 + (i % 5) * 130, 100 + (i // 5) * 150
            self.canvas.create_image(x, y, image=photo, anchor="center")
            self.canvas.create_text(x, y + 70, text=file.replace(".png", ""), fill="white")
            self.root.image = photo  # Prevent garbage collection

    def run(self):
        self.load_sigils()
        self.display_sigils()
        self.root.mainloop()


if __name__ == "__main__":
    browser = SigilArchiveBrowser()
    browser.run()
