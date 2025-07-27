from flask import Flask, jsonify
import paramiko
import os

app = Flask(__name__)

HOST = os.getenv("SFTP_HOST", "de3.bot-hosting.net")
PORT = int(os.getenv("SFTP_PORT", 2022))
USERNAME = os.getenv("SFTP_USERNAME", "")
PASSWORD = os.getenv("SFTP_PASSWORD", "")

@app.route("/health")
def health_check():
    try:
        transport = paramiko.Transport((HOST, PORT))
        transport.connect(username=USERNAME, password=PASSWORD)
        transport.close()
        return jsonify({"status": "OK"}), 200
    except Exception as e:
        return jsonify({"status": "FAILED", "error": str(e)}), 503

@app.route("/")
def home():
    return jsonify({"message": "SFTP monitor for de3.bot-hosting.net is live!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
