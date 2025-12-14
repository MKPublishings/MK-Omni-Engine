import tkinter as tk
from assets.overlays.sigil_dashboard import SigilDashboard


class MythicUI:

    def __init__(self):
        self.dashboard = SigilDashboard()
        self.root = tk.Tk()
        self.root.title("SlizzAi 5 Mythic Overlay")
        self.labels = {}

        for room in self.dashboard.rooms:
            label = tk.Label(self.root, text=f"{room.upper()}: [inactive]", font=("Consolas", 14))
            label.pack()
            self.labels[room] = label

        self.update_ui()

    def update_ui(self):
        for room, data in self.dashboard.ui.state.items():
            glyph = data.get("glyph", "—")
            status = data.get("status", "—")
            self.labels[room].config(text=f"{room.upper()}: {glyph} [{status}]")
        self.root.after(3000, self.update_ui)

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    ui = MythicUI()
    ui.dashboard.update_room("renderer", "SLIZZ-RENDER-002", "active")
    ui.dashboard.update_room("logic", "GLYPH-TRUTH", "invoked")
    ui.run()
