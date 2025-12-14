# engines/generation.py

class GenerationEngine:
    def run(self, input_data):
        prompt = input_data.replace("generate:", "").strip()
        return {"output": f"Generated content for: {prompt}"}