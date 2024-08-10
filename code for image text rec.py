import cv2
import pytesseract
from langdetect import detect


pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

def read_image_and_detect_language(image_path, lang='eng'):

    image = cv2.imread(image_path)
    
    if image is None:
        raise FileNotFoundError(f"Could not open or find the image: {image_path}")

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

   
    text = pytesseract.image_to_string(gray, lang=lang)

    language = detect(text)

    return text, language

image_path = r'kannada_test_sample.png'  #Path to your Kannada image file
try:
    extracted_text, detected_language = read_image_and_detect_language(image_path, lang='kan')
    print(f"Extracted Text:\n{extracted_text}")
    print(f"Detected Language: {detected_language}")
except FileNotFoundError as e:
    print(e)
