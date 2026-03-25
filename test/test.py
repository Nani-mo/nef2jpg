import time
from pathlib import Path

import rawpy
from PIL import Image  # pillow

avr_time = []
# Ordner des Scripts
script_dir = Path("test_data/")  # Pfad zum Ordner in dem sich alles befindet
name_rec_dir = "/unedit/"  # des des Unterordners, indem die convertierten Bilder gespeichert werden
print("Verzeichnis: ", str(script_dir))


def main():

    count_files(script_dir)
    inp = str(input("want to proceed: [Y/n]"))
    if inp.lower() == "n" or "no":
        exit()

    start = time.perf_counter()
    mem_nef, mem_not = 0, 0
    for file0 in script_dir.iterdir():
        if file0.is_dir():  # ist das Objekt ueberhaupt ein Ordner, wenn es eine Datei ist --> skip
            Path(str(file0) + name_rec_dir).mkdir(exist_ok=True)  # erstellt Ordner, ueberspring, wenn schon existent
            for file1 in file0.iterdir():
                if file1.suffix.lower() == ".nef":
                    mem_nef = mem_nef + 1  # nef Zaehler
                    processing_image(file0, file1, mem_nef)
                else:
                    mem_not = mem_not + 1

    end = time.perf_counter()

    # auswertng
    avr = 0
    for i in avr_time:
        avr = avr + i
    avr = avr / float(len(avr_time))

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
    img.save(
        str(file0) + name_rec_dir + str(file1.name)[:-4] + ".jpg",
        quality=100,
    )
    end = time.perf_counter()

    avr_time.append(end - start)

    print(
        f"picture prossed [{mem_nef}]: ",
        str(file1.name),
        "    ",
        f"{end - start:.1f}s",
    )
    # print(str(file0) + name_rec_dir + str(file1.name)[:-4] + ".jpg")


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

    print("time: ", end - start, "s\n", "NEF files: ", mem_nef, "    ", "non NEF files :", mem_not)


try:
    main()
except KeyboardInterrupt:
    exit()


# zaehlt alle .NEF dateien auf, fragt dann ob alle convertiert sollen
# Frage wie der Zeilordner heißen soll
#
# Zeit fuer ein picture processing
#
# Endstatistik:
#
# avarage Zeit fuer ein Bild
# Gesammt Zeit die es gebraucht hat
