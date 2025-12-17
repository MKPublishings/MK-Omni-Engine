import networkx as nx
import matplotlib.pyplot as plt


class CodexConstellation:

    def __init__(self):
        self.graph = nx.Graph()

    def add_codex(self, name, glyphs):
        self.graph.add_node(name, glyphs=glyphs)
        for glyph in glyphs:
            self.graph.add_node(glyph)
            self.graph.add_edge(name, glyph)

    def render_constellation(self):
        pos = nx.spring_layout(self.graph)
        plt.figure(figsize=(10, 8))
        nx.draw(self.graph, pos, with_labels=True, node_color="skyblue", edge_color="gray", font_size=10)
        plt.title("🌌 SlizzAi Codex Constellation")
        plt.show()


if __name__ == "__main__":
    mapper = CodexConstellation()
    mapper.add_codex("Codex X", ["GLYPH-TRUTH", "GLYPH-RENDER"])
    mapper.add_codex("Codex Y", ["GLYPH-ECHO", "GLYPH-RECLAIM"])
    mapper.render_constellation()
