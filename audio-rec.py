import speech_recognition as sr
import keyboard
import threading

stop_listening = False

def listen_for_key():
    global stop_listening
    while True:
        if keyboard.is_pressed('q'):
            stop_listening = True
            break

def recognize_kannada_speech():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    print("Listening for Kannada speech... (press 'q' to stop)")

    key_listener = threading.Thread(target=listen_for_key)
    key_listener.start()

    try:
        while True:
            if stop_listening:
                print("\nStop key pressed. Stopping...")
                break

            with mic as source:
                recognizer.adjust_for_ambient_noise(source)
                print("Say something in Kannada...")
                audio = recognizer.listen(source)

            try:
                print("Recognizing speech in Kannada...")
                text = recognizer.recognize_google(audio, language="kn-IN")
                print(f"Transcription: {text}")
            except sr.UnknownValueError:
                print("Could not understand the audio")
            except sr.RequestError as e:
                print(f"Could not request results from Google Speech Recognition service; {e}")

    except KeyboardInterrupt:
        print("\nStopped listening.")

    key_listener.join()

if __name__ == "__main__":
    recognize_kannada_speech()
