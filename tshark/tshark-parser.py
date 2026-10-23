import subprocess
import json
import time
import os
import argparse
import utils
import tomllib
from dataclasses import dataclass

# Read Defaults from config
with open("config.toml", "rb") as f:
    config = tomllib.load(f)

# Use hardcoded defaults as fallback if config missing
@dataclass
class TsharkParserDefaults:
    count: str = "1"
    port: str = "53"
    intSelection: int = 0

raw = config.get("DEFAULTS", {})

settings = TsharkParserDefaults(
    count=str(raw["count"]),
    port=str(raw["port"]),
    intSelection=int(raw["intSelection"])
)


packets = []

# Create a set of interfaces found on host
netInterfaces = os.listdir('/sys/class/net')
netInterfaces.insert(0, "any") # Add to index 0 (start)

print("_____Tshark Parser_____")
options = [
    f"[0] Interface: {netInterfaces[settings.intSelection]}",
    f"[1] Port: {settings.port}",
    f"[2] Packet Count: {settings.count}"
]
for i, option in enumerate(options, 0):
    print(options[i])

userInput = input(f"(Choose an option or hint enter to begin with defaults): ")

# Work in progress..
if userInput == "":
    utils.runParser(netInterfaces[settings.intSelection], settings.count, settings.port)
elif userInput == "0":
    print("Interface Selection: ")
elif userInput == "1":
    print("Enter desired port: ")
elif userInput == "2":
    print("Enter desired packet count: ")

