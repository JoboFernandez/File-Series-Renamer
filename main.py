import os
import re
import sys


screen_width = 70
sample_files = ["Game of Thrones-1.mp4", "Game of Thrones-02.mkv", "GOT 3.mp4"]
sample_settings = ["Title prefix: 'Game of Thrones'", "Title suffix: ' Season 8'", "Digits: 2"]
sample_output = ["Game of Thrones 01 Season 8.mp4", "Game of Thrones 02 Season 8.mkv",
                     "Game of Thrones 03 Season 8.mp4"]


def print_divider():
    print("*" * screen_width)

def print_heading():
    print_divider()
    print("WELCOME TO FILE SERIES RENAMER!".center(screen_width))
    print("below is a run-through of how this program is expected to work".center(screen_width))
    print_divider()

def print_sample(sample_title, lst):
    print(sample_title)
    for sample in lst:
        print(sample)

def print_samples():
    print_sample("\nSample files inside a folder: ", sample_files)
    print_sample("\nSample settings: ", sample_settings)
    print_sample("\nExpected filenames in the same folder: ", sample_output)

def rename_files():
    running = True
    while running:
        print()
        print_divider()
        print("Sample folder directory:")
        print("C:/Users/Username/Documents/Foldername")

        valid = False
        while not valid:
            folder = input("PLEASE ENTER FOLDER DIRECTORY: ")
            if not os.path.exists(folder):
                print("[!] Cannot locate the given folder path.")
                continue
            valid = True

        print_sample("\nSample files: ", sample_output)
        print("Title prefix: 'Game of Thrones'")
        print("Title suffix: ' Season 8'")
        print("Digit count: 2 --> 01, 02, 03, ..., 98, 99, 100, 101, ...")
        rename_prefix = input("PLEASE ENTER FILE TITLE PREFIX: ")
        rename_suffix = input("PLEASE ENTER FILE TITLE SUFFIX: ")

        valid = False
        while not valid:
            digits = input("PLEASE ENTER NUMBER OF DIGITS FOR TITLE COUNTER: ")
            if not digits.isnumeric():
                print("[!] Digit/s must be of numeric value.")
                continue
            digits = int(digits)
            valid = True

        print()

        print("[START]")
        pattern = re.compile(r"\d+")
        os.chdir(folder)
        for ep_title in os.listdir():
            ep_numbers = pattern.findall(ep_title)
            if not ep_numbers:
                print(f"[!] Failed to rename {ep_title}. Title number not found.")
                continue
            ep_number = ep_numbers[0].lstrip("0")
            ext_name = os.path.splitext(ep_title)[-1]

            new_number = ep_number.zfill(digits)
            new_title = f"{rename_prefix}{new_number}{rename_suffix}{ext_name}"
            os.rename(ep_title, new_title)

            print(f"Successfully renamed file {new_number}")

        print("[FINISH]\n")

        valid = False
        while not valid:
            again = input("Would you like to rename another set of files? (y/n): ")
            if again.lower() not in ["y", "n"]:
                print("[!] Answer not recognized.")
                continue
            valid = True
            if again.lower() == "n":
                print("[X] Program terminated.")
                sys.exit()

def main():
    print_heading()
    print_samples()
    rename_files()


if __name__ == "__main__":
    main()