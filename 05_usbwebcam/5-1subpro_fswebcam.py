#execute a cmd in python
import subprocess

#$fswebcam -r 640x480 --rotate 180 --jpeg 95 option.jpg
cmd = [
    "fswebcam",
    "-r", "640x480",
    "--rotate", "180",
    "--jpeg", "95",
    "photo_py.jpg"
]

subprocess.run(cmd)
