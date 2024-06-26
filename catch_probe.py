import os
from dotenv import load_dotenv
import scapy.all as scapy
# import pyshark

load_dotenv()

interface_name = os.getenv("INTERFACE_NAME")
if not interface_name:
    print("Error: INTERFACE_NAME environment variable is not set")
    exit(1)

print(f"Using interface: {interface_name}")

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
    # # Capture using pyshark
    # capture = pyshark.LiveCapture(interface=interface_name)
    # try:
    #     for packet in capture.sniff_continuously():
    #         if 'IP' in packet:
    #             src_ip = packet.ip.src
    #             dst_ip = packet.ip.dst
    #             protocol = packet.highest_layer
    #             print(f"Packet: {protocol} {src_ip} -> {dst_ip}")
    # except KeyboardInterrupt:
    #     print("Packet capture stopped by user.")
except Exception as e:
    print(f"Error: {e}")

print("")

for mac_addr, ssids in probe_requests.items():
    print(f"MAC Address: {mac_addr}, Frequently Used APs: {', '.join(ssids)}")

print('EXIT')

# https://www.blackbox.ai/publish/B2who_P5q-gCbGhNwnrjX
