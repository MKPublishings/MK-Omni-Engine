# 🧿 SlizzAi Codex X — Ritual Core
import time
from glyph_summoner_with_sigil import load_glyph
from assets.overlays.load_overlay import load_overlay
from legacy_archive.echo_logs import log_echo


def invoke_ritual(glyph_id, overlay_name="default_glyph", log_mode="echo", voice_enabled=False):
    try:
        glyph = load_glyph(glyph_id)
        overlay = load_overlay(overlay_name)
    except Exception as e:
        print(f"❌ Ritual Failed: Unable to load glyph or overlay.\n🪬 Error: {e}")
        return

    print(f"\n🔮 Invoking Ritual: {glyph_id}")
    print(f"🖼️ Overlay Bound: {overlay_name}")
    if voice_enabled:
        print("🎙️ Voice Invocation: Enabled")

    try:
        overlay.display(glyph_id)
    except Exception as e:
        print(f"⚠️ Overlay Display Error: {e}")
        return

    if log_mode == "echo":
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
        try:
            log_echo(f"🕰️ Glyph {glyph_id} rendered at {timestamp}")
        except Exception as e:
            print(f"📛 Logging Failed: {e}")

    print("✅ Ritual Complete\n")
