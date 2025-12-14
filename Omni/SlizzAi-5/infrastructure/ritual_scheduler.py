import time
import threading
from infrastructure.legacy_sync import LegacySync
from rooms.renderer_room import RendererRoom


class RitualScheduler:

    def __init__(self):
        self.sync = LegacySync()
        self.renderer = RendererRoom()

    def start(self):
        threading.Thread(target=self.schedule_sync).start()
        threading.Thread(target=self.schedule_pulse).start()

    def schedule_sync(self):
        while True:
            time.sleep(300)  # Every 5 minutes
            print("⏳ Scheduled Legacy Sync")
            self.sync.sync_all()

    def schedule_pulse(self):
        while True:
            time.sleep(180)  # Every 3 minutes
            print("🌐 Scheduled Glyph Pulse")
            self.renderer.pulse_glyph("SLIZZ-SCHEDULED-001")


if __name__ == "__main__":
    scheduler = RitualScheduler()
    scheduler.start()
