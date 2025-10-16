import os
from flask import Flask, jsonify
from water_loader.py import load_water_summary  # NOTE: see next line for correct import

# If the above import line errors, use this one instead (GitHub sometimes needs relative import):
# from water_loader import load_water_summary

app = Flask(__name__)

@app.route("/")
def home():
    summary = load_water_summary()
    return (
        "<h1>Lucy with Water</h1>"
        "<p>Alive ✅</p>"
        f"<pre>{summary}</pre>"
    )

@app.route("/status")
def status():
    return jsonify({"ok": True, "service": "LucyWithWater", "version": "1.0.0"})

if __name__ == "__main__":
    port = int(os.getenv("PORT", "10000"))
    # 0.0.0.0 so Render can reach it
    app.run(host="0.0.0.0", port=port)
