import scapy.all as scapy
import os
from dotenv import load_dotenv, dotenv_values 
load_dotenv() 

# Set the interface to monitor mode
### scapy.conf.iface = os.getenv("INTERFACE_NAME") # Uncumment this and create .env in order for this to work
# Create a dictionary to store the probe requests
probe_requests = {}

# Define a function to process the probe requests
def process_probe_request(pkt):
    if pkt.haslayer(scapy.Dot11) and pkt.type == 0 and pkt.subtype == 4:
        mac_addr = pkt.addr2
        ssid = pkt.info.decode()
        if mac_addr not in probe_requests:
            probe_requests[mac_addr] = []
        if ssid not in probe_requests[mac_addr]:
            probe_requests[mac_addr].append(ssid)

# Start sniffing in monitor mode
scapy.sniff(prn=process_probe_request, filter="", monitor=True)

# Print the probe requests
for mac_addr, ssids in probe_requests.items():
    print(f"MAC Address: {mac_addr}, Frequently Used APs: {', '.join(ssids)}")
