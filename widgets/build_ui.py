
import pathlib
import subprocess as sub

for path in pathlib.Path.cwd().glob("*.ui"):
    outpath = pathlib.Path(f"{path.stem}.py")
    build_cmd = [r'C:\Users\warre\anaconda3\Scripts\pyuic5', "-o", str(outpath), str(path)]
    print(f"INFO: Creating: ui -> py: {' '.join(build_cmd)}")
    sub.call(build_cmd)
    outpath.write_text(outpath.read_text().replace("import resources_rc", "from resources import resources"))