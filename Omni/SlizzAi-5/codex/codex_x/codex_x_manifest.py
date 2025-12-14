import os
import json
from datetime import datetime


class CodexXManifest:

    def __init__(self, output_path="CodexX_Legacy_Manifest.txt"):
        self.output_path = output_path
        self.sections = []

    def log_section(self, title, content):
        self.sections.append(f"\n## {title}\n{content}")

    def gather_glyphs(self):
        glyph_dir = "summoned_glyphs"
        if not os.path.exists(glyph_dir):
            return "No summoned glyphs found."
        glyphs = os.listdir(glyph_dir)
        return "\n".join([f"- {g}" for g in glyphs])

    def gather_sigils(self):
        sigil_dir = "sigil_archive"
        if not os.path.exists(sigil_dir):
            return "No sigils found."
        sigils = os.listdir(sigil_dir)
        return "\n".join([f"- {s.replace('.png','')}" for s in sigils if s.endswith(".png")])

    def gather_invocations(self):
        log_path = "ritual_logs/invocation_ledger.txt"
        if not os.path.exists(log_path):
            return "No invocations logged."
        with open(log_path, "r") as f:
            return f.read()

    def finalize_manifest(self):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        header = f"🧿 Codex X Legacy Manifest\nGenerated: {timestamp}\n\n"
        self.log_section("Summoned Glyphs", self.gather_glyphs())
        self.log_section("Sigil Archive", self.gather_sigils())
        self.log_section("Invocation Ledger", self.gather_invocations())
        self.log_section("System Components", "\n".join([
            "- Ritual Console",
            "- Echo Reincarnator",
            "- Mythic Chain Protocol",
            "- Legacy Witness UI",
            "- Unified Ritual Dashboard",
            "- Sigil Generator & Mapper",
            "- Sigil Archive Browser",
            "- Sigil Evolution Engine"
        ]))
        with open(self.output_path, "w") as f:
            f.write(header + "\n".join(self.sections))
        print(f"📜 Codex X Manifest saved at {self.output_path}")


if __name__ == "__main__":
    manifest = CodexXManifest()
    manifest.finalize_manifest()
