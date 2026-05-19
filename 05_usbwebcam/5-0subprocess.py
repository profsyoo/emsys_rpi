#execute a cmd in python
import subprocess

cmd = [
    "fswebcam",
    "-r", "640x480",
    "--rotate, "180"
    "--jpeg", "95",
    "photo_py.jpg"
]

subprocess.run(cmd)
