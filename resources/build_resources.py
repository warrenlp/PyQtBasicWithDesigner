
import pathlib
import subprocess as sub

for path in pathlib.Path.cwd().glob("*.qrc"):
    # Needed to run pip install pyqt5-tools
    build_cmd = [r'C:\Users\warre\anaconda3\Scripts\pyrcc5', "-o", f"{path.stem}.py", str(path)]
    print(f"INFO: Creating: qrc -> py: {' '.join(build_cmd)}")
    sub.call(build_cmd)
