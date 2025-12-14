from core.glyph_math import evaluate_glyph
from legacy_archive.echo_logs import log_echo


class LogicRoom:

    def __init__(self):
        self.state = {}

    def invoke_decision(self, glyph, context):
        result = evaluate_glyph(glyph, context)
        self.state[glyph] = result
        log_echo(f"🧠 Decision invoked: {glyph} → {result}")
        return result


if __name__ == "__main__":
    room = LogicRoom()
    decision = room.invoke_decision("GLYPH-TRUTH", {"input": 42})
    print(f"🔮 Decision Result: {decision}")
