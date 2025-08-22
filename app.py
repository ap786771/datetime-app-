from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def get_datetime():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"<h1>Current Date & Time:</h1><p>{now}</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
