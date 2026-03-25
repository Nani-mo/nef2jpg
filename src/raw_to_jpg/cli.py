import sys
import time
from importlib.resources import files
from pathlib import Path

import rawpy
from PIL import Image  # pillow
from rich.console import Console
from rich.markdown import Markdown

avr_time = []
name_rec_dir = "unedit"  # name for folder of new pictures


def main():
    if len(sys.argv) > 1:  # wurde überhaupt ein Argument übergeben
        if str(sys.argv[1]) == "-h" or str(sys.argv[1]) == "--help":  # eruzeugt --help -h
            console = Console()  # Datei in Terminal
            with files("raw_to_jpg").joinpath("README.en.md").open() as f:  # Ersatz fuer man page
                md = Markdown(f.read())  #
            console.print(md)  #
            exit()  #

        print(sys.argv)
        script_dir = Path(sys.argv[1])  # sys.argv -> 0= BEfehl Name, 1=flag den du zu Befehl übergibst
    else:
        script_dir = Path(".")  # path zu Ort des commands
    # Ordner des Scripts
    print("Verzeichnis: ", str(script_dir))

    nef = count_files(script_dir)
    if nef > 0:
        inp = str(input("want to proceed [Y/n]: "))
        if inp.lower() == "n" or inp.lower() == "no":
            print("exit")
            exit()
    else:
        print("zero .NEF files found - end process")
        exit()

    start = time.perf_counter()
    mem_nef, mem_not = 0, 0
    for file0 in script_dir.iterdir():
        if file0.is_dir():  # ist das Objekt ueberhaupt ein Ordner, wenn es eine Datei ist --> skip
            (file0 / name_rec_dir).mkdir(exist_ok=True)  # erstellt Ordner, ueberspring, wenn schon existent
            for file1 in file0.iterdir():
                if file1.suffix.lower() == ".nef":
                    mem_nef = mem_nef + 1  # nef Zaehler
                    processing_image(file0, file1, mem_nef)
                else:
                    mem_not = mem_not + 1

    end = time.perf_counter()

    # auswertng
    avr = sum(avr_time) / float(len(avr_time)) if avr_time else 0

    print(
        "NEF files: ",
        mem_nef,
        "  no NEF files: ",
        mem_not,
        f"\ntime: {end - start:.1f}s",
        f"\navrage time: {avr:.2f}s",
    )


def processing_image(file0, file1, mem_nef):

    start = time.perf_counter()

    with rawpy.imread(str(file1)) as raw:
        rgb = raw.postprocess(
            use_camera_wb=True,
            # use_camera_matrix=True,  # Kamera-Farbmatrix verwenden
            no_auto_bright=False,
            highlight_mode=2,  # blend – beste Lichterwiederherstellung
            gamma=(1.5, 4.5),  # sRGB Gamma
            output_color=rawpy.ColorSpace(2),
            output_bps=8,
        )

    img = Image.fromarray(rgb)
    img.save(file0 / name_rec_dir / (file1.stem + ".jpg"), quality=100)
    end = time.perf_counter()

    avr_time.append(end - start)

    print(
        f"picture prossed [{mem_nef}]: ",
        str(file1.name),
        "    ",
        f"{end - start:.1f}s",
    )


def count_files(script_dir):
    start = time.perf_counter()
    mem_nef, mem_not = 0, 0
    for file0 in script_dir.iterdir():
        if file0.is_dir():
            for file1 in file0.iterdir():
                if file1.suffix.lower() == ".nef":
                    mem_nef = mem_nef + 1  # nef Zaehler
                else:
                    mem_not = mem_not + 1  # non nef Zaehler
    end = time.perf_counter()

    print(f"time: {end - start:.4f}", "s\n", "NEF files: ", mem_nef, "    ", "non NEF files :", mem_not)
    return mem_nef


if __name__ == "__main__":
    main()
