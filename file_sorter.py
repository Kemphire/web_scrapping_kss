from pathlib import Path
import shutil

cwd = Path.cwd()

this_file = Path(__file__)

def make_dir(file: Path) -> Path:
  ft = file.suffix
  if len(str(ft)) > 1:
    dir_name = str(ft)[1:]
    dir = cwd / (dir_name + "s")
  else:
    dir = cwd / "nones"
  dir.mkdir(exist_ok=True)
  return dir

for file in cwd.glob("*"):
  if not (file.is_dir() or file == this_file):
    print(f"Found {file}")
    dir_in_which_to_add = make_dir(file)
    print(f"Moving {file} to {dir_in_which_to_add}")
    shutil.move(file, dir_in_which_to_add)
    print(f"Moved {file} to {dir_in_which_to_add}")

