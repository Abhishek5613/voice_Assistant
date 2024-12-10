import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes


def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("Recognizing...")
            data = recognizer.recognize_google(audio)
            return data
        except sr.UnknownValueError:
            return "Sorry, I did not understand that."
        except sr.RequestError:
            return "Sorry, I am having trouble accessing the recognition service."

def speechtx(X):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 150)
    engine.say(X)
    engine.runAndWait()

if __name__ == "__main__":
    data1 = sptext().lower()

    if "your name" in data1:
        name = "poonam chaurasia "
        speechtx(name)
    # else:
    #     speechtx("MCA 3rd sem")
    elif 'youtube' in data1:
        webbrowser.open("https://www.youtube.com/")
    elif 'physics' in data1:
        webbrowser.open("https://www.youtube.com/physicswallah")
    elif 'joke' in data1:
        joke_1 = pyjokes.get_joke(language="en",category="neutral")
        print(joke_1)
        speechtx(joke_1)
    
    