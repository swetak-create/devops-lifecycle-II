from flask import Flask, render_template_string

app = Flask(__name__)

html = """
<!DOCTYPE html>
<html>
<head>
    <title>AIML DevOps Batch</title>
    <style>
        body {
            background-color: black;
            color: cyan;
            font-size: 40px;
            font-family: Arial, sans-serif;
            overflow: hidden;
        }
        .move {
            position: absolute;
            white-space: nowrap;
            animation: moveText 8s linear infinite;
        }
        @keyframes moveText {
            from { left: -400px; }
            to { left: 100%; }
        }
    </style>
</head>
<body>
    <div class="move">🚀 AIML DEVOPS BATCH 🚀</div>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(html)

if __name__ == "__main__":
    app.run(debug=True)
