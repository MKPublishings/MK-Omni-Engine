from flask import Flask, render_template_string

app = Flask(__name__)


@app.route("/")
def witness_home():
    with open("legacy_archive/invocation_ledger.txt", "r") as f:
        ledger = f.read()
    return render_template_string("""
        <html>
        <head><title>Legacy Witness</title></head>
        <body>
            <h1>🧿 SlizzAi 5 Ritual History</h1>
            <pre>{{ ledger }}</pre>
        </body>
        </html>
    """, ledger=ledger)


if __name__ == "__main__":
    app.run(port=5052)
