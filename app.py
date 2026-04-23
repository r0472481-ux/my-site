from flask import Flask, render_template
import os
import json

app = Flask(__name__)

DATA_FILE = os.path.join(os.path.dirname(__file__), "data.json")

def load_data():
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

@app.route("/")
def home():
    profile = load_data()
    return render_template("index.html", profile=profile)

import os

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))