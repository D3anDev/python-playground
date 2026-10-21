import subprocess

output = subprocess.run(["tshark", "-i", "any", "-c", "5"]).stdout

print(output)