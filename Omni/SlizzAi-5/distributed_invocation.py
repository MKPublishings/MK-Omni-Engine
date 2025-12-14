import requests


class DistributedInvoker:

    def __init__(self, nodes):
        self.nodes = nodes  # List of node URLs

    def invoke_glyph(self, command):
        for node in self.nodes:
            try:
                response = requests.post(f"{node}/invoke", json={"command": command})
                print(f"🌐 Invoked on {node}: {response.json()}")
            except Exception as e:
                print(f"⚠️ Failed to invoke on {node}: {e}")


# Example usage
if __name__ == "__main__":
    nodes = ["http://localhost:5051", "http://192.168.1.10:5051"]
    invoker = DistributedInvoker(nodes)
    invoker.invoke_glyph("render glyph")
