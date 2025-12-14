import os


def generate_manifest(root="slizzai-5"):
    manifest = []
    for dirpath, dirnames, filenames in os.walk(root):
        for file in filenames:
            path = os.path.join(dirpath, file)
            manifest.append(path.replace("\\", "/"))
    with open("Codex_Manifest.md", "w") as f:
        f.write("# 🧾 SlizzAi 5 Codex Manifest\n\n")
        for entry in manifest:
            f.write(f"- `{entry}`\n")
    print("📜 Codex Manifest Generated")


if __name__ == "__main__":
    generate_manifest()
