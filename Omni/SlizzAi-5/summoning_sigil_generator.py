import tkinter as tk
import hashlib
import random


class SummoningSigilGenerator:

    def __init__(self, phrase):
        self.phrase = phrase
        self.root = tk.Tk()
        self.root.title("🧿 Summoning Sigil")
        self.root.geometry("600x600")
        self.canvas = tk.Canvas(self.root, bg="black")
        self.canvas.pack(fill="both", expand=True)

    def hash_phrase(self):
        return hashlib.sha256(self.phrase.encode()).hexdigest()

    def draw_sigil(self):
        hash_val = self.hash_phrase()
        center_x, center_y = 300, 300
        radius = 100

        for i in range(0, len(hash_val), 4):
            angle = int(hash_val[i:i + 2], 16) % 360
            length = int(hash_val[i + 2:i + 4], 16) % 80 + 20
            x = center_x + length * random.choice([-1, 1])
            y = center_y + length * random.choice([-1, 1])
            color = "#" + hash_val[i:i + 6]
            self.canvas.create_line(center_x, center_y, x, y, fill=color, width=2)
            self.canvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill=color)

        self.canvas.create_text(center_x, center_y, text=self.phrase, fill="white", font=("Helvetica", 12, "bold"))

    def run(self):
        self.draw_sigil()
        self.root.mainloop()


if __name__ == "__main__":
    phrase = input("🔮 Enter summoning phrase: ")
    sigil = SummoningSigilGenerator(phrase)
    sigil.run()
