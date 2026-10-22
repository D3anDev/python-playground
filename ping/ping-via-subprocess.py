import subprocess
from pathlib import Path

log_path = Path("log.txt")
if log_path.exists():
    print("Log File Exists. Adding to file...")
else:
    log_path.touch()
    print("No File Found. Creating Log File...")

ip_addresses = ["192.168.1.1", "192.168.10.1", "192.168.20.1"]

output = ""

for i, ip in enumerate(ip_addresses):
    output += subprocess.run(["ping", ip, "-c", "1"], capture_output=True, text=True).stdout


with open("output.log", "w") as f:
    f.write(output)
