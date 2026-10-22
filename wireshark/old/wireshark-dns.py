import subprocess
import json
import time

count = "1" #1 Line since we are digging into DNS data
port = "53" #DNS
packets = []
try:
    print("Waiting for traffic...")
    # Uses tshark (Wireshark cli), any interface, count of 1 packet, filters for DNS traffic, in JSON format
    output = subprocess.run(
        ["tshark", "-i", "any", "-c", count, "-f", "port " + port, "-T", "json"],
        capture_output=True,
        text=True
    )
    #print("Arguments Used \n", output.args)
    #print("Errors: \n", output.stderr)
    #print("Traffic: \n", output.stdout)
    packets = json.loads(output.stdout)
    
    pass
except FileNotFoundError:
    print("File Not Found!")
    pass
except json.JSONDecodeError:
    print("Failed to Parse JSON (Did Wireshark capture anything?")
    time.sleep(2)
    pass

for i, packet in enumerate(packets, 1):
    # Onion Mental Model
    # First unwrap the source layer
    source_dict = packet.get("_source", {})
    # Using the first layer to find and peel inner layer
    layers = source_dict.get("layers", {})
    # Then get the DNS layer
    dns_layer = layers.get("dns", {})
    # Prints i's DNS data and formats with json.dumps (will be a single packet because count is 1^^^)
    print(f"Packet # {i} DNS Layer:\n {json.dumps(dns_layer, indent=2)}")
