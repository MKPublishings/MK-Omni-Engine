import subprocess

subprocess.run(["git", "clone", "git@github.com:Slizzurp/SlizzAi-2.0.git"], check=True)
subprocess.run(["cd", "SlizzAi-2.0"], shell=True, check=True)