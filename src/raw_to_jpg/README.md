# NEF → JPG Converter

Ein Python-Script zur automatischen Konvertierung von Nikon RAW-Dateien (`.nef`) in JPEG-Bilder.

## Beschreibung

Das Script durchsucht alle Unterordner eines angegebenen Verzeichnisses nach `.nef`-Dateien und konvertiert diese in hochwertige JPEGs. Die konvertierten Bilder werden jeweils in einem Unterordner namens `unedit` innerhalb des ursprünglichen Ordners gespeichert.

## Installation

Im Root-Ordner des Projektes:

```bash
uv tool install .
```

Für eine erneute Installation:

```bash
uv tool install . --reinstall
```

## Verwendung

```bash
nef2jpg [Pfad zum Verzeichnis]
```

Wird kein Pfad angegeben, wird das aktuelle Verzeichnis verwendet:

```bash
nef2jpg
```

Die `-h`- oder `--help`-Flag zeigt diese Dokumentation direkt im Terminal an:

```bash
nef2jpg -h
```

```bash
nef2jpg --help
```

### Beispiel

```bash
nef2jpg /home/user/fotos
```

## Verzeichnisstruktur

Das Script erwartet folgende Struktur als Eingabe:

```
fotos/
├── session_01/
│   ├── IMG_001.nef
│   ├── IMG_002.nef
│   └── ...
└── session_02/
    ├── IMG_010.nef
    └── ...
```

Nach der Ausführung wird die Struktur wie folgt erweitert:

```
fotos/
├── session_01/
│   ├── unedit/
│   │   ├── IMG_001.jpg
│   │   └── IMG_002.jpg
│   ├── IMG_001.nef
│   └── IMG_002.nef
└── session_02/
    ├── unedit/
    │   └── IMG_010.jpg
    └── IMG_010.nef
```

## Ablauf

1. Das Script zählt zunächst alle NEF- und Nicht-NEF-Dateien und gibt eine Übersicht aus.
2. Der Nutzer wird gefragt, ob die Konvertierung gestartet werden soll (`[Y/n]`).
3. Jede NEF-Datei wird verarbeitet und als JPEG gespeichert.
4. Am Ende wird eine Zusammenfassung mit Dateianzahl und Zeitstatistiken ausgegeben.

## Konvertierungseinstellungen

| Parameter | Wert | Beschreibung |
|---|---|---|
| Weißabgleich | Kamera-WB | Übernimmt den WB der Kamera |
| Helligkeit | Auto | Automatische Helligkeitsanpassung aktiv |
| Lichter | Blend (Modus 2) | Beste Lichterwiederherstellung |
| Gamma | (1.5, 4.5) | sRGB-Gamma |
| Farbraum | sRGB | Standard-Farbraum |
| Bittiefe | 8 Bit | Standard JPEG |
| JPEG-Qualität | 100 | Maximale Qualität |

## Ausgabe (Beispiel)

```
Verzeichnis:  /home/user/fotos
time: 0.0021 s
NEF files:  42     non NEF files: 5
want to proceed [Y/n]: Y
picture prossed [1]:  IMG_001.NEF     2.3s
picture prossed [2]:  IMG_002.NEF     2.1s
...
NEF files:  42   no NEF files:  5
time: 97.4s
avrage time: 2.32s
```

## Hinweise

- Nur direkte Unterordner des angegebenen Verzeichnisses werden durchsucht (keine rekursive Suche).
- Bereits vorhandene `unedit`-Ordner werden nicht überschrieben, sondern wiederverwendet.
- Dateien ohne `.nef`-Endung werden übersprungen und mitgezählt.
- crazy nightcore: `https://www.youtube.com/watch?v=uVoqIP4M9Gg`
