import os
import re


SCREEN_WIDTH = 70
NUMBER_PATTERN = re.compile(r"\d+")
sample_files = [
    "Game of Thrones-1.mp4",
    "Game of Thrones-02.mkv",
    "GOT 3.mp4"
]
sample_settings = [
    "Title prefix: 'Game of Thrones'",
    "Title suffix: ' Season 8'",
    "Digits: 2"
]
sample_output = [
    "Game of Thrones 01 Season 8.mp4",
    "Game of Thrones 02 Season 8.mkv",
    "Game of Thrones 03 Season 8.mp4"
]


def print_heading():
    print("*" * SCREEN_WIDTH)
    print("WELCOME TO FILE SERIES RENAMER!".center(SCREEN_WIDTH))
    print("below is a run-through of how this program is expected to work".center(SCREEN_WIDTH))
    print("*" * SCREEN_WIDTH)


def print_sample(sample_title: str, lst: list):
    print(sample_title)
    for sample in lst:
        print(sample)


def print_samples():
    print_sample("\nSample files inside a folder: ", sample_files)
    print_sample("\nSample settings: ", sample_settings)
    print_sample("\nExpected filenames in the same folder: ", sample_output)


def rename_files():
    print()
    print("*" * SCREEN_WIDTH)

    # ask for folder directory
    print("Sample folder directory:")
    print("C:/Users/Username/Documents/Foldername")
    while True:
        folder = input("PLEASE ENTER FOLDER DIRECTORY: ")
        if os.path.exists(folder):
            break
        print("[!] Cannot locate the given folder path.")

    # ask for file name prefix and suffix
    print_sample("\nSample files: ", sample_output)
    print("Title prefix: 'Game of Thrones'")
    print("Title suffix: ' Season 8'")
    print("Digit count: 2 --> 01, 02, 03, ..., 98, 99, 100, 101, ...")
    rename_prefix = input("PLEASE ENTER FILE TITLE PREFIX: ")
    rename_suffix = input("PLEASE ENTER FILE TITLE SUFFIX: ")

    # ask for file number padding
    while True:
        digits = input("PLEASE ENTER NUMBER OF DIGITS FOR TITLE COUNTER: ")
        if digits.isnumeric():
            digits = int(digits)
            break
        print("[!] Digit/s must be of numeric value.")
    print()

    # start renaming file
    print("[START]")
    os.chdir(folder)
    for ep_title in os.listdir():

        # check for file series number
        ep_numbers = NUMBER_PATTERN.findall(ep_title)
        if not ep_numbers:
            print(f"[!] Failed to rename {ep_title}. Title number not found.")
            continue

        # rename file
        ep_number = ep_numbers[0].lstrip("0")
        ext_name = os.path.splitext(ep_title)[-1]
        new_number = ep_number.zfill(digits)
        new_title = f"{rename_prefix}{new_number}{rename_suffix}{ext_name}"
        os.rename(ep_title, new_title)
        print(f"Successfully renamed file {new_number}")
    print("[FINISH]\n")


if __name__ == "__main__":
    print_heading()
    print_samples()
    rename_files()