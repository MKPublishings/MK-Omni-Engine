# renderer.py

import cv2
from qiskit import QuantumCircuit
from qiskit.visualization import circuit_drawer
import os

class StrRenderer:
    """
    Renderer for SlizzAi-4 Rituals — handles quantum circuit visualization and symbolic overlays.
    """
    
    def __init__(self):
        print("🖼️ Renderer initialized for SlizzAi-4 Rituals.")
        self.output_dir = "render_output"
        os.makedirs(self.output_dir, exist_ok=True)
        print(f"🖼️ Renderer initialized. Output directory: {self.output_dir}"
        )

class Renderer:
    """
    SlizzAi Visual Ritual Engine — renders quantum circuits and symbolic overlays.
    """

    def __init__(self, output_dir="render_output"):
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)
        print(f"🖼️ Renderer initialized. Output directory: {self.output_dir}")

    def render_circuit(self, qc: QuantumCircuit, filename: str = "circuit.png"):
        """
        Render a quantum circuit to an image file.
        """
        try:
            circuit_drawer(qc, output='mpl', filename=os.path.join(self.output_dir, filename))
            print(f"🎨 Quantum circuit rendered to {filename}")
        except Exception as e:
            print(f"⚠️ Failed to render circuit: {e}")
            return None

    def overlay_entropy_glyph(self, base_image_path: str, delta_H: float, filename: str = "glyph_overlay.png"):
        """
        Overlay entropy glyph (symbolic text) onto an image.
        """
        try:
            img = cv2.imread(base_image_path)
            if img is None:
                raise FileNotFoundError(f"Image not found at {base_image_path}")

            overlay_text = f"Ξα(ψ) ΔH = {delta_H:.4f}"
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(img, overlay_text, (50, 50), font, 1, (255, 0, 255), 2, cv2.LINE_AA)

            path = os.path.join(self.output_dir, filename)
            cv2.imwrite(path, img)
            print(f"🧬 Entropy glyph overlay saved to {path}")
            return path
        except Exception as e:
            print(f"⚠️ Failed to overlay glyph: {e}")
            return None

    def show_image(self, image_path: str):
        """
        Display an image using OpenCV.
        """
        try:
            img = cv2.imread(image_path)
            if img is None:
                raise FileNotFoundError(f"Image not found at {image_path}")
            cv2.imshow("SlizzAi Ritual Image", img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        except Exception as e:
            print(f"⚠️ Failed to display image: {e}")