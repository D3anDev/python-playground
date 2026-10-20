# Day One of learning python, using my bash experience as a bridge

# To use bash commands inside of Python
import subprocess

# Variables to handle paths
src = input("Enter Source Path: ")
dest = input("Enter Destination Path: ")

# From my mental model
# Runs rsync with -avp flags
# Appends the variables taken from input for src and dest
# Runs as if it's a bash command
try:
    subprocess.run(["rsync", "-avP", src, dest])
    print("\n[+] Sync Completed Successfully!")
except KeyboardInterrupt:
    print("\n[!] Sync canceled by user!")