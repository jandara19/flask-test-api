import os
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # lets the React app (different origin) call this API

@app.route("/test", methods=["GET"])
def test():
    return jsonify({"message": "test done"})

@app.route("/env", methods=["GET"])
def env_value():
    return jsonify({"value": os.environ.get("APP_MESSAGE", "not set")})
    
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
