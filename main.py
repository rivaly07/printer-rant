from pathlib import Path
import os


def main():
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    rant = "My printer says ‘Ready’ while holding my page hostage. Then it flashes ‘PC LOAD LETTER’—which I believe is printer for ‘I can see the paper, but I need you to lose an afternoon.’"
    (output_dir / "entry.txt").write_text(rant, encoding="utf-8")


if __name__ == "__main__":
    main()
