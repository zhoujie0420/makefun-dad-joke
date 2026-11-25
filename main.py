"""Dad Joke Showdown entry generator."""
import pathlib
import sys

# Entry text
TEXT = "Our crossword club's attendance is down this year, but the regulars keep coming across."

def main():
    out = pathlib.Path("/output")
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(TEXT, encoding="utf-8")
    print("Entry written successfully.", file=sys.stderr)

if __name__ == "__main__":
    main()


