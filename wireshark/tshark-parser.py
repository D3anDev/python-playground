import subprocess
import json
import time
import os

# Defaults
count = "1"
port = "53" 
intSelection = 0  
packets = []

# Create a set of interfaces found on host
netInterfaces = os.listdir('/sys/class/net')
# By default chooses "any" interface (meaning all on the current host)
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

if userInput == "":
    try:
        print(f"Waiting for traffic on Interface {netInterfaces[intSelection]}...")
        # Uses tshark (Wireshark cli), any interface, count of 1 packet, filters for DNS traffic, in JSON format
        output = subprocess.run(
            ["tshark", "-i", netInterfaces[intSelection], "-c", count, "-f", "port " + port, "-T", "json"],
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
        # DNS Info:
        dns_layer = layers.get("dns", {})
        # IP Info:
        ip_layer = layers.get("ip", {})
        ip_src = ip_layer.get("ip.src")
        ip_src_host = ip_layer.get("ip.src_host")
        ip_dst = ip_layer.get("ip.dst")
        ip_dst_host = ip_layer.get("ip.dst_host")

        #print(f"Packet # {i} Info:\n {json.dumps(layers, indent=2)}")
        print(f"Source IP: {ip_src}")
        print(f"Source Host: {ip_src_host}")
        print(f"Destination IP: {ip_dst}")
        print(f"Destination Host: {ip_dst_host}")
pass
