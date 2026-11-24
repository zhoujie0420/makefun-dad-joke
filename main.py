import pathlib

TEXT = "Our crossword club's attendance is down this year, but the regulars keep coming across."

out = pathlib.Path("/output")
out.mkdir(parents=True, exist_ok=True)
(out / "entry.txt").write_text(TEXT, encoding="utf-8")
