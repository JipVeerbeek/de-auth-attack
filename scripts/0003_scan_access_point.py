import subprocess

def scan_access_points(interface):
    command = "sudo airodump-ng " + interface
    output = subprocess.check_output(command, shell=True).decode("utf-8")
    aps = []
    for line in output.split("\n"):
        if "BSSID" in line:
            continue
        columns = line.split()
        if len(columns) >= 6:
            bssid = columns[0]
            essid = columns[5]
            aps.append((bssid, essid))
    return aps

interface = '' # Monitor interface
aps = scan_access_points(interface)
print("Access points found:")
for i, (bssid, essid) in enumerate(aps):
    print(f"{i+1}. {essid} ({bssid})")