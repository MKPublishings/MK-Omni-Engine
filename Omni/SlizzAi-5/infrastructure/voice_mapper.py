class VoiceGlyphMapper:

    def __init__(self):
        self.map = {
            "render glyph": "RendererRoom.pulse_glyph",
            "invoke decision": "LogicRoom.invoke_decision"
        }

    def learn_trigger(self, phrase, action):
        self.map[phrase] = action
        print(f"🧬 Learned new trigger: '{phrase}' → {action}")

    def get_action(self, phrase):
        return self.map.get(phrase, "unrecognized_glyph")


# Example usage
if __name__ == "__main__":
    mapper = VoiceGlyphMapper()
    mapper.learn_trigger("sync archive", "ArchiveRoom.sync_logs")
    print(mapper.get_action("sync archive"))
