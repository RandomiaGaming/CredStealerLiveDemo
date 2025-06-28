domain = "notreallychase.com"
certConf = f"""
[req]
default_bits       = 2048
prompt             = no
default_md         = sha256
x509_extensions    = req_ext
distinguished_name = dn

[dn]
C  = US
ST = Oregon
L  = Portland
O  = FinlayTheBerry
CN = {domain}

[req_ext]
subjectAltName = @alt_names

[alt_names]
DNS.1 = {domain}
DNS.2 = www.{domain}
"""

import os
import subprocess

os.makedirs("cert", exist_ok=True)
with open("cert/cert.conf", "w", encoding="utf-8") as certConfFile:
    certConfFile.write(certConf)
subprocess.run(f"\"C:\\Program Files\\Git\\usr\\bin\\openssl.exe\" req -x509 -newkey rsa:2048 -nodes -keyout cert/notreallychase.com.key -out cert/notreallychase.com.crt -config cert/cert.conf -days 365", shell=True)

print()
print("Press any key to exit...")
input()