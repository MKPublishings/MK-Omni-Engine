import speech_recognition as sr


def listen_for_glyph():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🔊 Awaiting invocation...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            return command.lower()
        except sr.UnknownValueError:
            return "unrecognized_glyph"
