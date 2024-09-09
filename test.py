from pathlib import Path
from PIL import Image
import pytesseract

print(pytesseract.image_to_string(Image.open("IMG_2609.jpg")))