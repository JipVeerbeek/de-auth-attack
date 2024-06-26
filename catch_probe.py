import scapy.all as scapy
import os
from dotenv import load_dotenv

load_dotenv()

interface_name = os.getenv("INTERFACE_NAME")
if not interface_name:
    print("Error: INTERFACE_NAME environment variable is not set")
    exit(1)

print(f"Using interface: {interface_name}")

scapy.conf.iface = interface_name

probe_requests = {}

def process_probe_request(pkt):
    if pkt.haslayer(scapy.Dot11) and pkt.type == 0 and pkt.subtype == 4:
        mac_addr = pkt.addr2
        ssid = pkt.info.decode()
        if mac_addr not in probe_requests:
            probe_requests[mac_addr] = []
        if ssid not in probe_requests[mac_addr]:
            probe_requests[mac_addr].append(ssid)
        print(f"Captured probe request: {mac_addr} -> {ssid}")

try:
    scapy.sniff(prn=process_probe_request, iface=interface_name)
except Exception as e:
    print(f"Error: {e}")

print("")

for mac_addr, ssids in probe_requests.items():
    print(f"MAC Address: {mac_addr}, Frequently Used APs: {', '.join(ssids)}")

print('EXIT')
