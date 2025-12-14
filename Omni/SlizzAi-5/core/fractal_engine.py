def generate_fractal(seed, depth):
    if depth == 0:
        return [seed]
    echo = seed * depth
    return [echo] + generate_fractal(seed, depth - 1)


def generate_fractal(seed, depth, echo_log=None):
    if depth == 0:
        return [seed]
    echo = seed * depth
    if echo_log:
        echo_log(f"🔁 Fractal echo: {echo}")
    return [echo] + generate_fractal(seed, depth - 1, echo_log)

