#!/usr/bin/env python3
"""
SlizzAi-3.3: Standalone and Cloud AI Image Generator & Chat
===========================================================
- Local or cloud deployment
- OpenAI GPT chat + DALL-E image generation (extendable to Stable Diffusion/PyTorch)
- PyQt5 GUI with improved threading safety & prompt refinement

Author: SlizzAi Team
"""

import sys
import os
import threading
import openai
import requests
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QTextEdit,
    QLabel, QPushButton, QListWidget, QSplitter, QProgressBar
)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, pyqtSignal

# --- Configuration ---
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    print("[Warning] No API key found. Set OPENAI_API_KEY environment variable.")
openai.api_key = OPENAI_API_KEY
class SlizzAiApp(QWidget):
    update_chat_signal = pyqtSignal(str)
    update_image_signal = pyqtSignal(QPixmap)

    def __init__(self):
        super().__init__()
        self.setWindowTitle("SlizzAi v3.3 Standalone")
        self.resize(1200, 800)
        self.init_ui()
        self.update_chat_signal.connect(self.update_chat)
        self.update_image_signal.connect(self.update_image)

    def init_ui(self):
        splitter = QSplitter(Qt.Orientation.Horizontal)

        # --- Left: Chatroom ---
        self.chat_list = QListWidget()
        self.chat_input = QTextEdit()
        self.chat_input.setPlaceholderText("Type your message...")
        self.send_chat_btn = QPushButton("Send")
        self.send_chat_btn.clicked.connect(self.send_chat)

        left_layout = QVBoxLayout()
        left_layout.addWidget(QLabel("Chatroom (OpenAI + SlizzAi)"))
        left_layout.addWidget(self.chat_list)
        left_layout.addWidget(self.chat_input)
        left_layout.addWidget(self.send_chat_btn)
        left_widget = QWidget()
        left_widget.setLayout(left_layout)

        # --- Center: Prompt Console ---
        self.prompt_input = QTextEdit()
        self.prompt_input.setPlaceholderText("Enter prompt for text/image...")
        self.analyze_btn = QPushButton("Analyze/Generate")
        self.analyze_btn.clicked.connect(self.analyze_prompt)

        center_layout = QVBoxLayout()
        center_layout.addWidget(QLabel("Prompt Console"))
        center_layout.addWidget(self.prompt_input)
        center_layout.addWidget(self.analyze_btn)
        center_widget = QWidget()
        center_widget.setLayout(center_layout)

        # --- Right: Image Tab ---
        self.image_label = QLabel("Generated images appear here.")
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.progress_bar = QProgressBar()
        self.progress_bar.hide()

        right_layout = QVBoxLayout()
        right_layout.addWidget(QLabel("Image Tab"))
        right_layout.addWidget(self.image_label)
        right_layout.addWidget(self.progress_bar)
        right_widget = QWidget()
        right_widget.setLayout(right_layout)

        splitter.addWidget(left_widget)
        splitter.addWidget(center_widget)
        splitter.addWidget(right_widget)

        main_layout = QVBoxLayout()
        main_layout.addWidget(splitter)
        self.setLayout(main_layout)

    def send_chat(self):
        user_msg = self.chat_input.toPlainText().strip()
        if not user_msg:
            return
        self.chat_list.addItem(f"You: {user_msg}")
        self.chat_input.clear()
        threading.Thread(target=self.get_openai_chat, args=(user_msg,)).start()

    def get_openai_chat(self, prompt):
        try:
            response = openai.chat.completions.create(
                model="gpt-4o",
                messages=[{"role": "user", "content": prompt}]
            )
            reply = response.choices[0].message.content
        except Exception as e:
            reply = f"[Error] {e}"
        self.update_chat_signal.emit(f"SlizzAi: {reply}")

    def update_chat(self, message):
        self.chat_list.addItem(message)

    def analyze_prompt(self):
        prompt = self.prompt_input.toPlainText().strip()
        if not prompt:
            return
        if prompt.lower().startswith("image:"):
            image_prompt = prompt[6:].strip()
            threading.Thread(target=self.generate_image, args=(image_prompt,)).start()
        else:
            self.chat_list.addItem(f"You: {prompt}")
            threading.Thread(target=self.get_openai_chat, args=(prompt,)).start()

    def generate_image(self, prompt):
        try:
            self.progress_bar.show()
            refined_prompt = prompt
            try:
                refine_response = openai.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                        {"role": "system", "content": "Refine this prompt for high-quality image generation."},
                        {"role": "user", "content": prompt}
                    ]
                )
                content = refine_response.choices[0].message.content
                refined_prompt = content.strip() if content is not None else prompt
            except Exception as e:
                # If refinement fails, use the original prompt
                refined_prompt = prompt

            response = openai.images.generate(
                model="dall-e-3",
                prompt=refined_prompt,
                n=1,
                size="1024x1024"
            )
            # Access the image URL from the response object
            img_url = None
            if response.data and isinstance(response.data, list) and len(response.data) > 0:
                img_url = getattr(response.data[0], "url", None)
            if not img_url or not isinstance(img_url, str):
                raise ValueError("No valid image URL returned from OpenAI API.")
            img_data = requests.get(img_url).content
            pixmap = QPixmap()
            pixmap.loadFromData(img_data)
            self.update_image_signal.emit(pixmap.scaled(512, 512, Qt.AspectRatioMode.KeepAspectRatio))
        except Exception as e:
            self.image_label.setText(f"[Image generation error] {e}")
        finally:
            self.progress_bar.hide()

    def update_image(self, pixmap):
        self.image_label.setPixmap(pixmap)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SlizzAiApp()
    window.show()
    sys.exit(app.exec_())
# --- End of SlizzAi-3.3.py ---
# Note: Ensure you have the required packages installed: PyQt5, openai, requests, and PIL.
# This code is a standalone application that integrates OpenAI's GPT and DALL-E for chat and image generation.
# It can be extended to support Stable Diffusion or other models as needed.
