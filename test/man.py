import subprocess
from pathlib import Path

from rich.console import Console
from rich.text import Text
from rich.theme import Theme


def show_manpage(filepath=Path("nef2jpg.1")):
    # groff wandelt .1 → Plain text mit ANSI
    result = subprocess.run(["groff", "-man", "-Tutf8", filepath], capture_output=True, text=True)
    text = result.stdout
    console = Console()
    console.print(text)


show_manpage()


"""
import os
import subprocess
from pathlib import Path


def show_manpage(filepath):
    filepath = Path(filepath)
    env = os.environ.copy()
    env["MANPAGER"] = "less -R"  # ANSI-Farben durchlassen
    env["GROFF_NO_SGR"] = "1"  # Overstrikes statt SGR (für manche Systeme)

    # man kann direkte Pfade mit -l öffnen
    subprocess.run(["man", "-l", str(filepath)], env=env)


show_manpage("nef2jpg.1")
"""
"""
from rich.console import Console
from rich.markdown import Markdown

console = Console()

with open("README.md") as f:
    md = Markdown(f.read())

console.print(md)
"""
