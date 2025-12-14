def log_echo(message):
    with open("legacy_archive/echo_logs.md", "a") as log_file:
        log_file.write(f"{message}\n")
