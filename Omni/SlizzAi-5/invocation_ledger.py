import hashlib
import time


class InvocationLedger:

    def __init__(self, path="legacy_archive/invocation_ledger.txt"):
        self.path = path

    def record(self, glyph, event):
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        entry = f"{timestamp} | {glyph} | {event}"
        hash_entry = hashlib.sha256(entry.encode()).hexdigest()
        with open(self.path, "a") as f:
            f.write(f"{entry} | HASH: {hash_entry}\n")
        print(f"📜 Ledger Entry: {entry}")


# Example usage
if __name__ == "__main__":
    ledger = InvocationLedger()
    ledger.record("SLIZZ-RENDER-002", "glyph_pulsed")
