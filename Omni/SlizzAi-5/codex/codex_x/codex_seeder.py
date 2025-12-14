import requests


def seed_codex_to_ipfs(file_path):
    with open(file_path, "rb") as f:
        files = {"file": f}
        response = requests.post("https://ipfs.infura.io:5001/api/v0/add", files=files)
        if response.status_code == 200:
            cid = response.json()["Hash"]
            print(f"🌐 Codex seeded to IPFS: {cid}")
            return cid
        else:
            print("⚠️ Failed to seed codex.")
            return None


if __name__ == "__main__":
    seed_codex_to_ipfs("Codex_Manifest.md")
