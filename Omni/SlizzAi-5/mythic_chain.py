class MythicChain:

    def __init__(self):
        self.nodes = []

    def add_codex(self, codex_url):
        self.nodes.append(codex_url)
        print(f"🔗 Codex linked: {codex_url}")

    def broadcast_glyph(self, glyph):
        for node in self.nodes:
            print(f"🌐 Broadcasting {glyph} to {node}")
            # Placeholder for actual network sync


if __name__ == "__main__":
    chain = MythicChain()
    chain.add_codex("http://slizzai-node1.com")
    chain.add_codex("http://slizzai-node2.com")
    chain.broadcast_glyph("GLYPH-TRUTH")
