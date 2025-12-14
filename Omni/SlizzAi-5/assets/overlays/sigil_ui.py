class SigilUI:

    def __init__(self):
        self.state = {}

    def update_sigil(self, room, glyph, status):
        self.state[room] = {"glyph": glyph, "status": status}
        self.display(room)

    def display(self, room):
        glyph = self.state[room]["glyph"]
        status = self.state[room]["status"]
        print(f"🧿 [{room.upper()}] → Glyph: {glyph} | Status: {status}")


# Example usage
if __name__ == "__main__":
    ui = SigilUI()
    ui.update_sigil("renderer", "SLIZZ-RENDER-002", "active")
