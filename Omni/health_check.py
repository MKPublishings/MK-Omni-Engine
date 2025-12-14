# health_check.py
def check_engines_status(engines):
    status = {}
    for name, engine in engines.items():
        try:
            status[name] = engine.ping()
        except Exception:
            status[name] = "DOWN"
    return status