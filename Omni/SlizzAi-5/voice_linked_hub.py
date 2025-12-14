import speech_recognition as sr
import tkinter as tk


class VoiceLinkedHUD:

    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.root = tk.Tk()
        self.root.title("🎙️ Voice-Linked HUD")
        self.root.geometry("600x400")
        self.canvas = tk.Canvas(self.root, bg="black")
        self.canvas.pack(fill="both", expand=True)

    def animate_glyph(self, glyph):
        self.canvas.delete("all")
        self.canvas.create_oval(250, 150, 350, 250, fill="blue")
        self.canvas.create_text(300, 200, text=glyph, fill="white", font=("Helvetica", 14, "bold"))

    def listen_and_animate(self):
        with sr.Microphone() as source:
            print("🎙️ Speak a glyph...")
            audio = self.recognizer.listen(source)

        try:
            spoken = self.recognizer.recognize_google(audio).upper()
            print(f"🔊 Heard: {spoken}")
            self.animate_glyph(spoken)
        except Exception as e:
            print(f"⚠️ Voice error: {e}")

    def run(self):
        self.root.after(1000, self.listen_and_animate)
        self.root.mainloop()


if __name__ == "__main__":
    hud = VoiceLinkedHUD()
    hud.run()
