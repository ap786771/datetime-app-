from flask import Flask
from datetime import datetime
from zoneinfo import ZoneInfo   # built-in in Python 3.9+

app = Flask(__name__)

@app.route("/")
def get_datetime():
    now = datetime.now(ZoneInfo("Asia/Kolkata"))  # IST timezone
    formatted_time = now.strftime("%Y-%m-%d %H:%M:%S %Z")
    return f"<h1>Current Date & Time (IST):</h1><p>{formatted_time}</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000)
