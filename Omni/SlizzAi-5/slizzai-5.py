# 🔮 SlizzAi 5 — Ritual Launcher
import argparse
from core.ritual_core import invoke_ritual


def main():
    parser = argparse.ArgumentParser(description="🌀 SlizzAi 5 — Glyph Invocation Protocol")
    parser.add_argument("--invoke", choices=["ritual"], required=True, help="Type of invocation")
    parser.add_argument("--glyph", type=str, required=True, help="Glyph ID to pulse")
    parser.add_argument("--overlay", type=str, default="default_glyph", help="Overlay to bind")
    parser.add_argument("--log", choices=["echo"], default="echo", help="Logging mode")
    parser.add_argument("--voice", choices=["on", "off"], default="off", help="Voice-triggered invocation")

    args = parser.parse_args()

    invoke_ritual(
        glyph_id=args.glyph,
        overlay_name=args.overlay,
        log_mode=args.log,
        voice_enabled=(args.voice == "on")
    )


if __name__ == "__main__":
    main()

# 🔮 SlizzAi 5 — Custom Ritual CLI
import argparse


def main():
    parser = argparse.ArgumentParser(
        description="🌀 SlizzAi 5 — Modular Glyph Invocation Engine",
        usage="slizzai-5.py --invoke {ritual} --glyph GLYPH [--overlay OVERLAY] [--log {echo}] [--voice {on,off}]"
    )

    parser.add_argument("--invoke", choices=["ritual"], required=True,
                        help="Type of invocation (ritual)")
    parser.add_argument("--glyph", type=str, required=True,
                        help="Glyph ID to pulse (e.g. SLIZZ-CORE-001)")
    parser.add_argument("--overlay", type=str, default="default_glyph",
                        help="Overlay to bind (default: default_glyph)")
    parser.add_argument("--log", choices=["echo"], default="echo",
                        help="Logging mode (default: echo)")
    parser.add_argument("--voice", choices=["on", "off"], default="off",
                        help="Enable voice-triggered invocation (default: off)")

    args = parser.parse_args()

    invoke_ritual(
        glyph_id=args.glyph,
        overlay_name=args.overlay,
        log_mode=args.log,
        voice_enabled=(args.voice == "on")
    )


if __name__ == "__main__":
    main()
