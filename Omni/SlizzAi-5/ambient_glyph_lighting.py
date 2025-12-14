import serial


class AmbientGlyphLighting:

    def __init__(self, port="COM3", baudrate=9600):
        self.ser = serial.Serial(port, baudrate)

    def trigger_lighting(self, glyph):
        color_map = {
            "GLYPH-TRUTH": "blue",
            "GLYPH-ECHO": "green",
            "GLYPH-RENDER-ASCENDED": "gold"
        }
        color = color_map.get(glyph, "white")
        self.ser.write(f"{color}\n".encode())
        print(f"🌈 Lighting triggered: {color} for {glyph}")


if __name__ == "__main__":
    lighting = AmbientGlyphLighting()
    lighting.trigger_lighting("GLYPH-TRUTH")
