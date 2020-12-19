# This is a sample Python script.

import subprocess
import optparse
import re

# re stands for regular expression


def get_argument():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="interface to change its MAC ADDRESS")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC ADDRESS")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[+++] Please enter your interface, use --help to get more info")
    elif not options.new_mac:
        parser.error("[+++] Please inter your MAC ADDRESS, use --help to get more info")
    return options


def mac_changer(interface,new_mac):
    print("[>>>] CHANGING MAC ADDRESS FOR " + interface + " TO " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
    if search_result:
        return search_result.group(0)
    else:
        print("[-] Could not read MAC ADDRESS")


options = get_argument()

current_mac_val = get_current_mac(options.interface)
print("Current MAC is => " + str(current_mac_val))

mac_changer(options.interface, options.new_mac)

current_mac_val = get_current_mac(options.interface)
if current_mac_val == options.new_mac:
    print("[+] MAC ADDRESS was successfully changed to " + current_mac_val)
else:
    print("[-] MAC ADDRESS did not get change.")

