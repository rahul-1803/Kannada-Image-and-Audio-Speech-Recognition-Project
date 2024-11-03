Here’s an updated version reflecting the use of Gradio for a multi-functional text recognition system:

---

# Kannada Multi-Function Text Recognition System

This project demonstrates a multi-functional system for recognizing Kannada speech and text using Python, now with an interactive Gradio interface. The system handles Kannada speech, image-based text, and real-time video text recognition across multiple languages. Key libraries include `speech_recognition`, `pytesseract`, `opencv-python`, and `langdetect`.

## Table of Contents

### Prerequisites
Before you begin, ensure you have the following software installed on your system:

- Python 3.7 or higher
- Tesseract OCR (for text recognition)

## Installation
1. Clone the repository: 
   ```bash
   git clone https://github.com/yourusername/kannada-text-recognition.git
   cd kannada-text-recognition
   ```

2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Make sure Tesseract OCR is installed on your system.

4. Update the path to the Tesseract executable in the Python scripts as needed:
   ```python
   pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
   ```

## Project Structure
- **app.py**: This main Gradio app combines all functionalities in a single, user-friendly interface, enabling Kannada speech recognition, image-based text recognition, and real-time camera text recognition.
  
- **speech_recognition.py**: Script to recognize Kannada speech through a microphone using the Google Speech Recognition API.

- **image_text_recognition.py**: Script to read images, convert them to grayscale, and extract Kannada text using Tesseract OCR, identifying the language with `langdetect`.

- **real_time_text_recognition.py**: Captures video from the webcam, performs real-time text extraction, and detects language for each frame.

## Usage
### Multi-Function Interface (app.py)
1. Run the Gradio app:
   ```bash
   python app.py
   ```
2. Open the displayed URL in your browser. You can then choose between Kannada speech recognition, image text recognition, or real-time camera text recognition.

### Kannada Speech Recognition (speech_recognition.py)
1. Run the script:
   ```bash
   python speech_recognition.py
   ```
2. Speak in Kannada, and the transcription will appear on the console.

### Kannada Image Text Recognition (image_text_recognition.py)
1. Place an image in the same directory as the script or specify its full path.
2. Run the script:
   ```bash
   python image_text_recognition.py
   ```
3. Extracted text and detected language are displayed on the console.

### Real-Time Text Recognition (real_time_text_recognition.py)
1. Ensure your webcam is connected and working.
2. Run the script:
   ```bash
   python real_time_text_recognition.py
   ```
3. The script displays the video feed with real-time text extraction and language detection. Press `q` to stop the camera.

