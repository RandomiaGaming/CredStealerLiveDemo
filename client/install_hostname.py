hostsPath = "C:\\Windows\\System32\\drivers\\etc\\hosts"

with open(hostsPath, "r", encoding="utf-8") as hostsFile:
    hostsContents = hostsFile.read()

if not "notreallychase.com" in hostsContents:
    with open(hostsPath, "a", encoding="utf-8") as hostsFile:
        hostsFile.write("\n")
        hostsFile.write("\n")
        hostsFile.write("127.0.0.1 notreallychase.com\n")
        hostsFile.write("127.0.0.1 www.notreallychase.com\n")

print()
print("Press any key to exit...")
input()