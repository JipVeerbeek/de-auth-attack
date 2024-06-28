import subprocess

def get_monitor_interface(interface):
    command = f"sudo airmon-ng start {interface}"
    output = subprocess.check_output(command, shell=True).decode("utf-8")
    monitor_interface = [line.split()[1] for line in output.split("\n") if "monitor mode enabled" in line][0]
    return monitor_interface

interface = '' # interface
monitor_interface = get_monitor_interface(interface)
print(f"Monitor interface: {monitor_interface}")