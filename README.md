# Kannada-Image-and-Audio-Speech-Recognition-Project
This project demonstrates the recognition of Kannada speech and text using Python. The repository contains three Python scripts, each focusing on different aspects of speech and text recognition using various libraries such as speech_recognition, pytesseract, opencv-python, and langdetect.

## Table of Contents

### Prerequisites
Before you begin, ensure you have the following software installed on your system:

Python 3.7 or higher
Tesseract OCR (for text recognition)

## Installation
1.Clone the repository: 
```
git clone https://github.com/yourusername/kannada-speech-text-recognition.git
 ```
```
cd kannada-speech-text-recognition
```

2.Install the required Python packages:
```
pip install -r requirements.txt
```
3.Make sure Tesseract OCR is installed on your system.

4.Update the path to the Tesseract executable in the Python scripts as needed:
```
pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
```

## Project Structure
speech_recognition.py: This script listens to Kannada speech through a microphone and transcribes it using the Google Speech Recognition API.

image_text_recognition.py: This script reads an image, converts it to grayscale, and extracts Kannada text using Tesseract OCR. The detected language is also identified using the langdetect library.

real_time_text_recognition.py: This script captures video from the webcam, extracts text from each frame in real time, and detects the language of the text.

## Usage
Kannada Speech Recognition (speech_recognition.py)
1.Run the script:
```
python speech_recognition.py
```

2.Speak in Kannada. The script will listen to your speech and display the transcription on the console.

3.Press q to stop the recognition.

## Kannada Image Text Recognition (image_text_recognition.py)
Place your image file in the same directory as the script or provide the full path to the image.

1.Run the script:
```
python image_text_recognition.py
```

2.The script will display the extracted text and the detected language.

# Real-Time Text Recognition (real_time_text_recognition.py)
1.Ensure your webcam is connected and working.

2.Run the script:
```
python real_time_text_recognition.py
```
3.The script will display the webcam feed, extract text in real time, and display the detected language. Press q to stop the camera.

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request or open an Issue for any bugs, features, or improvements.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
