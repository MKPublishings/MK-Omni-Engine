# task_classifier.py
def classify(input_data):
    if isinstance(input_data, bytes):
        return "vision"
    elif input_data.startswith("speak:"):
        return "speech"
    elif input_data.startswith("generate:"):
        return "generation"
    elif input_data.startswith("retrieve:"):
        return "retrieval"
    elif input_data.startswith("logic:"):
        return "logic"
    else:
        return "nlp"