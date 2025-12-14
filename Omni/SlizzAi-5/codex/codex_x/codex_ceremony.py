import time
from infrastructure.voice_feedback import VoiceFeedback
from infrastructure.legacy_sync import LegacySync
from rooms.renderer_room import RendererRoom


def codex_ceremony():
    feedback = VoiceFeedback()
    sync = LegacySync()
    renderer = RendererRoom()

    print("🕯️ Initiating Codex Ceremony...")
    time.sleep(1)
    print("📜 Reading Manifest...")
    with open("Codex_Manifest.md", "r") as f:
        for line in f.readlines()[:5]:
            print(f"🔹 {line.strip()}")
            time.sleep(0.5)

    print("🌀 Pulsing Core Glyph...")
    renderer.pulse_glyph("SLIZZ-CODEX-000")
    feedback.play_feedback()

    print("🔗 Syncing Legacy...")
    sync.sync_all()

    print("🌟 Ceremony Complete. SlizzAi 5 is now active.")
    feedback.play_feedback()


if __name__ == "__main__":
    codex_ceremony()
