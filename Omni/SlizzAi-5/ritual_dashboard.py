import threading
import time
from ambient_glyph_lighting import AmbientGlyphLighting
from echo_trail_visualizer import visualize_echo_trail
from voice_driven_reincarnator import VoiceReincarnator
from ritual_console import RitualConsole


class UnifiedRitualDashboard:

    def __init__(self):
        self.console = RitualConsole()
        self.lighting = AmbientGlyphLighting()
        self.reincarnator = VoiceReincarnator()

    def invoke_glyph(self):
        print("🎙️ Listening for invocation...")
        with self.console.recognizer.Microphone() as source:
            audio = self.console.recognizer.listen(source)

        try:
            command = self.console.recognizer.recognize_google(audio).lower()
            print(f"🔊 Heard: {command}")
            glyph = self.console.glyph_registry.get(command)
            if glyph:
                self.console.activate_glyph(glyph)
                self.lighting.trigger_lighting(glyph)
            else:
                print("❓ Unknown glyph command.")
        except Exception as e:
            print(f"⚠️ Invocation error: {e}")

    def rebirth_glyph(self):
        print("🎤 Listening for glyph ID to rebirth...")
        self.reincarnator.listen_and_rebirth()

    def show_echo_trail(self):
        print("🌀 Rendering echo trail...")
        visualize_echo_trail()

    def run_dashboard(self):
        print("🧿 Unified Ritual Dashboard Activated")
        while True:
            print("\n🔮 Choose ritual:")
            print("1. Invoke Glyph")
            print("2. Rebirth Glyph")
            print("3. Show Echo Trail")
            print("4. Exit")
            choice = input("→ ")

            if choice == "1":
                self.invoke_glyph()
            elif choice == "2":
                self.rebirth_glyph()
            elif choice == "3":
                self.show_echo_trail()
            elif choice == "4":
                print("🛑 Ritual Dashboard closed.")
                break
            else:
                print("❌ Invalid choice.")


if __name__ == "__main__":
    dashboard = UnifiedRitualDashboard()
    dashboard.run_dashboard()
