import json
from legacy_archive.echo_logs import log_echo


class ArchiveRoom:

    def __init__(self, archive_path="legacy_archive/glyph_history.json"):
        self.archive_path = archive_path
        self.archive = self.load_archive()

    def load_archive(self):
        try:
            with open(self.archive_path, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

    def sync_logs(self, new_glyph):
        self.archive[new_glyph] = {"timestamp": self._current_time()}
        self._save_archive()
        log_echo(f"📜 Synced glyph: {new_glyph}")
        print(f"✅ Archive updated with {new_glyph}")

    def _save_archive(self):
        with open(self.archive_path, "w") as f:
            json.dump(self.archive, f, indent=2)

    def _current_time(self):
        import time
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


if __name__ == "__main__":
    room = ArchiveRoom()
    room.sync_logs("SLIZZ-RENDER-002")
