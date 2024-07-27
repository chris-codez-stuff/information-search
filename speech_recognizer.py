import sounddevice as sd
import wavio
import speech_recognition as sr


def record_audio(filename, duration, fs):
    print("Recording...")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()
    wavio.write(filename, recording, fs, sampwidth=2)
    print("Recording complete")


def recognize_speech_from_audio(filename):
    recognizer = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")

    return ""


if __name__ == "__main__":
    fs = 44100  # Sample rate
    duration = 5  # Duration of recording
    filename = "output.wav"

    while True:
        choice = input("Choose an option:\n1. Record and Recognize Speech\n2. Text to Speech\n3. Exit\n")
        if choice == '1':
            record_audio(filename, duration, fs)
            recognized_text = recognize_speech_from_audio(filename)
            if recognized_text:
                print(f"Recognized Text: {recognized_text}")
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")
