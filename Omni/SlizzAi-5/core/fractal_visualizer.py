def visualize_fractal(seed, depth):
    trail = []
    for i in range(depth):
        echo = seed * (depth - i)
        trail.append(f"🔁 Depth {depth - i}: Echo {echo}")
    return trail


if __name__ == "__main__":
    trail = visualize_fractal(3, 5)
    for line in trail:
        print(line)
