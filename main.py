import os
import re

folder = "/home/username/Documents/Working/FilenameSeriesRenamer/TestFiles01"
rename_prefix = "File "
rename_suffix = ""
digits = 3

pattern = re.compile(r"\d+")
os.chdir(folder)
for ep_title in os.listdir():
    ep_number = pattern.findall(ep_title)[0].lstrip("0")
    ext_name = os.path.splitext(ep_title)[-1]

    new_number = ep_number.zfill(digits)
    new_title = f"{rename_prefix}{new_number}{rename_suffix}{ext_name}"
    os.rename(ep_title, new_title)

    print(f"Renamed file {new_number}")

print("Finished")