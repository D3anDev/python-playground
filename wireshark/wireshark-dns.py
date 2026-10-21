import subprocess

count = "10" #10 Lines
port = "53" #DNS

output = subprocess.run(
    ["tshark", "-i", "any", "-c", count, "-f", "port " + port],
    capture_output=True,
    text=True
)

print("Arguments Used \n", output.args)
print("Errors: \n", output.stderr)
print("Traffic: \n", output.stdout)
