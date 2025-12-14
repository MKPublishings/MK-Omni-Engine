from infrastructure.voice_listener import listen_for_glyph
from infrastructure.room_router import route_command


def voice_ritual_console():
    print("🎙️ Voice Ritual Console Activated")
    while True:
        command = listen_for_glyph()
        if command == "exit":
            print("🛑 Ritual Console Closed")
            break
        route_command(command)


if __name__ == "__main__":
    voice_ritual_console()
