import PyInstaller.__main__
import shutil
import pathlib

OUT_DIR="./Furious_VER"

def main():
    PyInstaller.__main__.run([
        'main.py',
        '-F',
        '-nFurious',
        '--icon=furious_emoji.ico',
        '--noconsole'
    ])
    shutil.copy("./dist/Furious.exe", f"{OUT_DIR}/Furious.exe")


if __name__ == "__main__":
    main()