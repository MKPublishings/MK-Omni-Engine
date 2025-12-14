from legacy_archive.echo_logs import log_echo


class ErrorReclaimer:

    def __init__(self):
        self.reclaimed = []

    def reclaim(self, error_phrase):
        glyph = f"RECLAIMED-{hash(error_phrase) % 10000}"
        self.reclaimed.append(glyph)
        log_echo(f"♻️ Error reclaimed: '{error_phrase}' → {glyph}")
        print(f"✅ Reclaimed glyph: {glyph}")
        return glyph


# Example usage
if __name__ == "__main__":
    reclaimer = ErrorReclaimer()
    reclaimer.reclaim("unrecognized_glyph")
