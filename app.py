import os
from flask import Flask, jsonify

# ---- inline replacement for water_loader.py ----
def _water_path():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_dir, "water.trf")

def load_water_summary():
    path = _water_path()
    if not os.path.exists(path):
        return "water.trf not found; using default resonance parameters."
    try:
        with open(path, "rb") as f:
            data = f.read()
        preview = data[:120]
        return f"water.trf size={len(data)} bytes; preview={preview!r}"
    except Exception as e:
        return f"Failed to read water.trf: {e}"
# ------------------------------------------------

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
    app.run(host="0.0.0.0", port=port)
