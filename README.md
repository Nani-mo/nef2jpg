# NEF → JPG Converter

A Python script for automatically converting Nikon RAW files (`.nef`) to JPEG images.

## Description

The script searches all subdirectories of a given directory for `.nef` files and converts them to high-quality JPEGs. The converted images are saved in a subfolder named `unedit` inside each original folder.

## Installation

From the root of the project:

```bash
uv tool install .
```

To reinstall:

```bash
uv tool install . --reinstall
```

## Usage

```bash
nef2jpg [path to directory]
```

If no path is provided, the current directory is used:

```bash
nef2jpg
```

The `-h` or `--help` flag displays this documentation directly in the terminal:

```bash
nef2jpg -h
```

```bash
nef2jpg --help
```

### Example

```bash
nef2jpg /home/user/photos
```

## Directory Structure

The script expects the following input structure:

```
photos/
├── session_01/
│   ├── IMG_001.nef
│   ├── IMG_002.nef
│   └── ...
└── session_02/
    ├── IMG_010.nef
    └── ...
```

After execution the structure is extended as follows:

```
photos/
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

## Process

1. The script counts all NEF and non-NEF files and prints a summary.
2. The user is asked whether to proceed (`[Y/n]`).
3. Each NEF file is processed and saved as a JPEG.
4. A final summary with file counts and timing statistics is printed.

## Conversion Settings

| Parameter | Value | Description |
|---|---|---|
| White balance | Camera WB | Uses the camera's white balance |
| Brightness | Auto | Automatic brightness adjustment enabled |
| Highlights | Blend (mode 2) | Best highlight recovery |
| Gamma | (1.5, 4.5) | sRGB gamma |
| Color space | sRGB | Standard color space |
| Bit depth | 8 bit | Standard JPEG |
| JPEG quality | 100 | Maximum quality |

## Example Output

```
directory:  /home/user/photos
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

## Notes

- Only direct subdirectories of the given path are searched (no recursive search).
- Existing `unedit` folders are reused without being overwritten.
- Files without a `.nef` extension are skipped and counted.
- crazy nightcore: `https://www.youtube.com/watch?v=uVoqIP4M9Gg`
