import random


class InvocationOracle:

    def __init__(self):
        self.echo_pool = ["GLYPH-TRUTH", "GLYPH-RENDER", "GLYPH-ECHO", "GLYPH-RECLAIM"]

    def divine_next(self):
        glyph = random.choice(self.echo_pool)
        print(f"🔮 Oracle whispers: Next glyph shall be {glyph}")

    def expand_pool(self, new_glyph):
        self.echo_pool.append(new_glyph)
        print(f"✨ Glyph {new_glyph} added to Oracle's pool.")


if __name__ == "__main__":
    oracle = InvocationOracle()
    oracle.expand_pool("GLYPH-LEGACY")
    oracle.divine_next()
