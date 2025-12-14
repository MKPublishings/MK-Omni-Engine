from rooms.renderer_room import RendererRoom
from rooms.logic_room import LogicRoom


def route_command(command):
    if "render" in command:
        RendererRoom().pulse_glyph("SLIZZ-RENDER-002")
    elif "decide" in command:
        LogicRoom().invoke_decision("GLYPH-TRUTH", {"input": 7})
    else:
        print(f"⚠️ Unknown command: {command}")
