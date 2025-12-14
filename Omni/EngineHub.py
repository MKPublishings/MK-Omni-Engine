class EngineHub:
    def __init__(self):
        self.vision = VisionModule()
        self.nlp = NLPModule()
        self.speech = SpeechModule()

    def run(self, input_data):
        if is_image(input_data):
            return self.vision.process(input_data)
        elif is_text(input_data):
            return self.nlp.respond(input_data)
        elif is_audio(input_data):
            return self.speech.transcribe(input_data)