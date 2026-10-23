from scapy.all import Ether, ARP, sendp

packet = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst="192.168.1.1")

sendp(packet)

# Note: Still working on this, my first attempt at making my own packet