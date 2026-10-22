import subprocess
import json
import time
import os
import argparse
import utils
import tomllib

# Read Defaults from config
with open("config.toml", "rb") as f:
    config = tomllib.load(f)

count = config.get("DEFAULTS", {}).get("count")
port = config.get("DEFAULTS", {}).get("port")
intSelection = config.get("DEFAULTS", {}).get("intSelection")

# Cast fix (temp)
count = str(count)
port = str(port)
intSelection = int(intSelection) 

packets = []

# Create a set of interfaces found on host
netInterfaces = os.listdir('/sys/class/net')
netInterfaces.insert(0, "any") # Add to index 0 (start)

print("_____Tshark Parser_____")
options = [
    f"[0] Interface: {netInterfaces[intSelection]}",
    f"[1] Port: {port}",
    f"[2] Packet Count: {count}"
]
for i, option in enumerate(options, 0):
    print(options[i])

userInput = input(f"(Choose an option or hint enter to begin with defaults): ")

# Work in progress..
if userInput == "":
    utils.runParser(netInterfaces[intSelection], count, port)
elif userInput == "0":
    print("Interface Selection: ")
elif userInput == "1":
    print("Enter desired port: ")
elif userInput == "2":
    print("Enter desired packet count: ")

