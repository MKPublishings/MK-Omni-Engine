import time
from legacy_archive.echo_logs import log_echo
from infrastructure.voice_memory import VoiceMemory
from rooms.archive_room import ArchiveRoom


class LegacySync:

    def __init__(self):
        self.archive = ArchiveRoom()
        self.voice_memory = VoiceMemory()

    def sync_all(self):
        log_echo("🔗 Legacy Sync Initiated")
        for entry in self.voice_memory.memory:
            glyph = f"VOICE-{hash(entry['phrase']) % 10000}"
            self.archive.sync_logs(glyph)
        log_echo("✅ Legacy Sync Complete")


if __name__ == "__main__":
    sync = LegacySync()
    sync.sync_all()
