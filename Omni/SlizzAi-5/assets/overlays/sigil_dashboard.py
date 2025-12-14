from assets.overlays.sigil_ui import SigilUI


class SigilDashboard:

    def __init__(self):
        self.ui = SigilUI()
        self.rooms = ["renderer", "logic", "archive"]

    def update_room(self, room, glyph, status):
        if room in self.rooms:
            self.ui.update_sigil(room, glyph, status)
        else:
            print(f"⚠️ Unknown room: {room}")

    def display_all(self):
        for room in self.rooms:
            self.ui.display(room)


# Example usage
if __name__ == "__main__":
    dashboard = SigilDashboard()
    dashboard.update_room("renderer", "SLIZZ-RENDER-002", "active")
    dashboard.update_room("logic", "GLYPH-TRUTH", "invoked")
    dashboard.display_all()
