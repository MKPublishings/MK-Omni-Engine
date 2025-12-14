import matplotlib.pyplot as plt


def visualize_echo_trail(log_path="ritual_logs/invocation_ledger.txt"):
    with open(log_path, "r") as f:
        lines = f.readlines()

    timestamps = []
    glyphs = []
    for line in lines:
        ts, _, glyph = line.partition("::")
        timestamps.append(ts.strip())
        glyphs.append(glyph.strip())

    plt.figure(figsize=(12, 6))
    plt.plot(timestamps, glyphs, marker="o", linestyle="-", color="purple")
    plt.xticks(rotation=45)
    plt.title("🌀 Echo Trail: Invocation History")
    plt.xlabel("Timestamp")
    plt.ylabel("Glyph")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    visualize_echo_trail()
