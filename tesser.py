import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract'

print(pytesseract.image_to_string(r'D:\\Git\\py-text\\image\\py1.png'))
