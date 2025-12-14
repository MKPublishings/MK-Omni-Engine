# slizzai_registry.py
import os

def index_modules(base_path="slizzai_engine"):
    registry = {}
    for root, _, files in os.walk(base_path):
        for file in files:
            if file.endswith(".py") and not file.startswith("__"):
                module_path = os.path.join(root, file)
                key = file.replace(".py", "")
                registry[key] = module_path
    return registry