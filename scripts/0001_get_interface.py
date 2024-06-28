import subprocess

def get_wireless_interface():
    command = "iwconfig"
    output = subprocess.check_output(command, shell=True).decode("utf-8")
    interfaces = [line.split()[0] for line in output.split("\n") if "IEEE" in line]
    if len(interfaces) > 1:
        print("Multiple wireless interfaces found. Please choose one:")
        for i, interface in enumerate(interfaces):
            print(f"{i+1}. {interface}")
        choice = int(input("Enter the number of the interface: "))
        interface = interfaces[choice-1]
    else:
        interface = interfaces[0]
    return interface

interface = get_wireless_interface()
print(f"Wireless interface: {interface}")
