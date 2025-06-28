import os
import shutil
import subprocess

# Update hostnames file
ip = input("Enter ip address for notreallychase.com: ")
print()
hostsPath = "C:\\Windows\\System32\\drivers\\etc\\hosts"
with open(hostsPath, "r", encoding="utf-8") as hostsFile: hostsContents = hostsFile.readlines()
hostsContents = [line for line in hostsContents if not "notreallychase.com" in line]
hostsContents.append(f"{ip} notreallychase.com\n")
hostsContents.append(f"{ip} www.notreallychase.com\n")
with open(hostsPath, "w", encoding="utf-8") as hostsFile: hostsFile.writelines(hostsContents)

# Reset user data dir
userDataFolderPath = os.path.abspath("chromeuserdata")
if os.path.exists(userDataFolderPath):
    shutil.rmtree(userDataFolderPath)
os.makedirs(userDataFolderPath, exist_ok=True)

# Launch chrome
subprocess.run(f"cmd /c start \"\" \"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe\" --user-data-dir=\"{userDataFolderPath}\" --no-first-run --disable-signin-promo --disable-features=PasswordManagerEnableSaving --disable-features=AutofillServerCommunication --disable-features=AutofillEnableAccountWalletStorage https://gmail.com", shell=True)

# Print manual setup instructions
print("Don't forget to install notreallychrome.com.crt at:")
print("chrome://certificate-manager/localcerts/usercerts")
print("and to disable the password manager at:")
print("chrome://password-manager/settings")
print("and to clear the error about google drive.")
print()

print("Press any key to exit...")
input()