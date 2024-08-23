# This code detects real time image through the camera to recognise Kannada text
import cv2
import pytesseract
from langdetect import detect
from langdetect.lang_detect_exception import LangDetectException

pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe" # Specify the path to Tesseract executable

def recognize_text_in_frame(frame, langs):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # Convert the frame to grayscale

    text = pytesseract.image_to_string(gray, lang=langs) # Perform OCR on the frame

    try:
        language_code = detect(text)
        if language_code == 'en':
            language = "English"
        elif language_code == 'kn':
            language = "Kannada"
        else:
            language = "Other"
    except LangDetectException:
        language = "Detection failed"

    return text, language


cap = cv2.VideoCapture(0) # Initialize the webcam

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

while True:
    ret, frame = cap.read() # Capture frame-by-frame

    if not ret:
        print("Error: Could not read frame.")
        break

    extracted_text, detected_language = recognize_text_in_frame(frame, langs='eng+kan') # Recognize text in the current frame

    # Display the extracted text on the frame
    cv2.putText(frame, f"Text: {extracted_text}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(frame, f"Language: {detected_language}", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2, cv2.LINE_AA)

    # Display the resulting frame
    cv2.imshow('Real-time Text Recognition', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'): # Press 'q' to exit camera
        break

cap.release()
cv2.destroyAllWindows()
