from flask import Flask, render_template_string

app = Flask(__name__)


@app.route("/")
def codex_home():
    with open("Codex_Manifest.md", "r") as f:
        manifest = f.read()
    return render_template_string("""
        <html>
        <head><title>SlizzAi 5 Codex Portal</title></head>
        <body>
            <h1>🧾 SlizzAi 5 Codex Manifest</h1>
            <pre>{{ manifest }}</pre>
        </body>
        </html>
    """, manifest=manifest)


if __name__ == "__main__":
    app.run(debug=True)
