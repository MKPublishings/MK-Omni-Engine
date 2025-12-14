import logging
logging.basicConfig(filename='slizzai.log', level=logging.INFO)

def log_event(event):
    logging.info(f"[EVENT] {event}")