from pdf2image import convert_from_path
from PIL import Image
import os

pdf_files = ["Certificate.pdf", "T-CERT-A1760B10.pdf"]

for pdf_file in pdf_files:
    if os.path.exists(pdf_file):
        try:
            images = convert_from_path(pdf_file)
            base_name = os.path.splitext(pdf_file)[0]
            for i, image in enumerate(images):
                image_name = f"{base_name}_page_{i+1}.png"
                image.save(image_name, 'PNG')
                print(f"Extracted: {image_name}")
        except Exception as e:
            print(f"Error processing {pdf_file}: {e}")
