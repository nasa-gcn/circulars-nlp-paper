"""
PNG to PDF Converter (Tight Layout, High Quality)
-------------------------------------------------
This script converts a PNG image to a PDF file with:
- No extra white borders (tight layout)
- Full image quality (no compression or scaling)
- Page size matching the image dimensions exactly

Usage (in terminal):
    python png_to_pdf_tight.py input_image.png [output_file.pdf]
"""

import fitz  # PyMuPDF for PDF generation
from PIL import Image  # Pillow for reading image size
import sys
import os

def png_to_pdf_tight(input_png, output_pdf=None):
    """Convert a PNG file to a high-quality, tight-layout PDF."""

    # Check if input file exists
    if not os.path.exists(input_png):
        raise FileNotFoundError(f"File not found: {input_png}")

    # If no output filename is given, use the same name with .pdf extension
    if output_pdf is None:
        output_pdf = os.path.splitext(input_png)[0] + ".pdf"

    # Get the width and height of the PNG image
    with Image.open(input_png) as img:
        width, height = img.size

    # Create a new PDF with one page matching the image dimensions
    pdf = fitz.open()
    page = pdf.new_page(width=width, height=height)

    # Insert the image into the page (fills the page exactly)
    page.insert_image(page.rect, filename=input_png, keep_proportion=True)

    # Save the PDF with no compression to keep full image quality
    pdf.save(output_pdf, deflate=False)
    pdf.close()

    print(f"PDF saved successfully: {output_pdf}")


if __name__ == "__main__":
    # Ensure the correct number of arguments
    if len(sys.argv) < 2:
        print("Usage: python png_to_pdf_tight.py <input.png> [output.pdf]")
        sys.exit(1)

    input_png = sys.argv[1]
    output_pdf = sys.argv[2] if len(sys.argv) > 2 else None

    png_to_pdf_tight(input_png, output_pdf)