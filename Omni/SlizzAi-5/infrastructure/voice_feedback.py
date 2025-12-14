import os
import random


class VoiceFeedback:

    def __init__(self, sound_dir="assets/sounds"):
        self.sounds = [f for f in os.listdir(sound_dir) if f.endswith(".mp3")]

    def play_feedback(self):
        if not self.sounds:
            print("🔇 No sound glyphs available.")
            return
        sound = random.choice(self.sounds)
        print(f"🔊 Playing sound glyph: {sound}")
        # Placeholder for actual playback logic


# Example usage
if __name__ == "__main__":
    vf = VoiceFeedback()
    vf.play_feedback()
