import os
import shutil
import subprocess

userDataFolderPath = os.path.abspath("chromeuserdata")

if os.path.exists(userDataFolderPath):
    shutil.rmtree(userDataFolderPath)
os.makedirs(userDataFolderPath, exist_ok=True)

subprocess.run(f"cmd /c start \"\" \"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe\" --user-data-dir=\"{userDataFolderPath}\" --no-first-run --disable-signin-promo https://gmail.com", shell=True)

print("Don't forget to install notreallychrome.com.crt at:")
print("chrome://certificate-manager/localcerts/usercerts")

print()
print("Press any key to exit...")
input()