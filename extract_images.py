import os
from PIL import Image
import io

try:
    import fitz  # PyMuPDF
    HAS_FITZ = True
except ImportError:
    HAS_FITZ = False

pdf_files = ["Certificate.pdf", "T-CERT-A1760B10.pdf"]

if HAS_FITZ:
    print("Using PyMuPDF to extract images...")
    import fitz
    for pdf_file in pdf_files:
        if os.path.exists(pdf_file):
            try:
                doc = fitz.open(pdf_file)
                base_name = os.path.splitext(pdf_file)[0]
                for page_num in range(len(doc)):
                    page = doc[page_num]
                    # Render page to image
                    pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))  # 2x zoom for quality
                    image_name = f"{base_name}_page_{page_num + 1}.png"
                    pix.save(image_name)
                    print(f"Extracted: {image_name}")
                doc.close()
            except Exception as e:
                print(f"Error processing {pdf_file}: {e}")
else:
    print("PyMuPDF not installed, attempting alternative method...")
    try:
        from pdf2image import convert_from_path
        print("Using pdf2image...")
        for pdf_file in pdf_files:
            if os.path.exists(pdf_file):
                try:
                    images = convert_from_path(pdf_file, dpi=200)
                    base_name = os.path.splitext(pdf_file)[0]
                    for i, image in enumerate(images):
                        image_name = f"{base_name}_page_{i+1}.png"
                        image.save(image_name, 'PNG')
                        print(f"Extracted: {image_name}")
                except Exception as e:
                    print(f"Error processing {pdf_file}: {e}")
    except ImportError:
        print("pdf2image not available")
