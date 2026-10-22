import subprocess
import json
import time
import os
import argparse

def runParser(netInterfaces, count, port):
    try:
        print(f"Waiting for traffic on Interface {netInterfaces}...")
        output = subprocess.run(
            ["tshark", "-i", netInterfaces, "-c", count, "-f", "port " + port, "-T", "json"],
            capture_output=True,
            text=True
        )
        #print("Arguments Used \n", output.args)
        #print("Errors: \n", output.stderr)
        #print("Traffic: \n", output.stdout)
        packets = json.loads(output.stdout)

    except KeyboardInterrupt:
        print("Canceled by user!")
        
    except FileNotFoundError:
        print("File Not Found!")

    except json.JSONDecodeError:
        print("Failed to Parse JSON (Did Wireshark capture anything?")
        time.sleep(2)
    
    for i, packet in enumerate(packets, 1):
        # Source layer
        source_dict = packet.get("_source", {})
        # Layers
        layers = source_dict.get("layers", {})
        # DNS Info:
        dns_layer = layers.get("dns", {})
        # IP Info:
        ip_layer = layers.get("ip", {})
        ip_src = ip_layer.get("ip.src")
        ip_src_host = ip_layer.get("ip.src_host")
        ip_dst = ip_layer.get("ip.dst")
        ip_dst_host = ip_layer.get("ip.dst_host")

        print(f"Packet # {i} Info:\n {json.dumps(layers, indent=2)}")
        # print(f"Source IP: {ip_src}")
        # print(f"Source Host: {ip_src_host}")
        # print(f"Destination IP: {ip_dst}")
        # print(f"Destination Host: {ip_dst_host}")
