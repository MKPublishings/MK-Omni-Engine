import json
import time


class VoiceMemory:

    def __init__(self, path="legacy_archive/voice_memory.json"):
        self.path = path
        self.memory = self.load_memory()

    def load_memory(self):
        try:
            with open(self.path, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def log_invocation(self, phrase):
        entry = {
            "phrase": phrase,
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
        }
        self.memory.append(entry)
        self.save_memory()
        print(f"🗣️ Invocation logged: {phrase}")

    def save_memory(self):
        with open(self.path, "w") as f:
            json.dump(self.memory, f, indent=2)


# Example usage
if __name__ == "__main__":
    vm = VoiceMemory()
    vm.log_invocation("render glyph")
