from flask import Flask, jsonify

app = Flask(__name__)
VERSION = "1.0.0"


@app.route("/")
def home():
    return jsonify(message="Hello DevOps!", version=VERSION)


@app.route("/health")
def health():
    return jsonify(status="ok"), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
