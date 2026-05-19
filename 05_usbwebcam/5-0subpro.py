#execute a cmd in python
import subprocess

#$ls -l images
cmd = [
    "ls",
    "-l",
    "images",
]
subprocess.run(cmd)
