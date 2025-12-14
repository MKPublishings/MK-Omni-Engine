from flask_limiter import Limiter
limiter = Limiter(key_func=get_remote_address)

@app.route("/run", methods=["POST"])
@limiter.limit("10 per minute")
def run_ai():
    ...