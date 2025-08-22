from flask import Flask
from datetime import datetime
from zoneinfo import ZoneInfo   # for IST timezone

app = Flask(__name__)

@app.route("/")
def get_datetime():
    now = datetime.now(ZoneInfo("Asia/Kolkata")).strftime("%Y-%m-%d %H:%M:%S %Z")
    
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Date Time App</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        <style>
            body {{
                background: linear-gradient(135deg, #FFA500, #FF7F50); /* orange gradient */
                height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                color: white;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            }}
            .card {{
                background: rgba(0,0,0,0.5);
                padding: 40px;
                border-radius: 20px;
                box-shadow: 0 8px 20px rgba(0,0,0,0.4);
                text-align: center;
            }}
            h1 {{
                font-size: 2.5rem;
                margin-bottom: 20px;
            }}
            p {{
                font-size: 1.8rem;
                font-weight: bold;
            }}
        </style>
    </head>
    <body>
        <div class="card">
            <h1>📅 Current Date & Time</h1>
            <p>{now}</p>
        </div>
    </body>
    </html>
    """
    return html_content

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000)
