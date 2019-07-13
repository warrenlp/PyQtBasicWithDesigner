import subprocess

subprocess.call([r'C:\ProgramData\Anaconda3\Library\bin\pyuic5.bat', "main.ui", ">", "main.py"])
subprocess.call([r'C:\ProgramData\Anaconda3\Library\bin\pyuic5.bat', "process_dialog.ui", ">", "process_dialog.py"])
