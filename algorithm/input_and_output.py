import speech_recognition as sr
import pyttsx3

def speak(msg, display):
    if display:
        print("Aura => " + str(msg))

    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 175)

    engine.say(msg)

    engine.runAndWait()
    engine.stop() 

def listen_input(): 
    r = sr.Recognizer()

    with sr.Microphone() as source:
        speak("Listening", True)
        audio = r.listen(source)

        try:
            cmd_rec = r.recognize_google(audio)
            cmd = str(cmd_rec).lower()
            print("You =>" + str(cmd_rec).capitalize())

            return cmd
        except sr.UnknownValueError:
            return "Pardon?"
        except sr.RequestError as e:
            print(str(e))
            speak("Error, could not request results from Google Speech Recognition services", True)

def yes_or_no(response):
    yeses = ["yes", "yeah", "yup", "yep", "sure"]
    for y in yeses:
        if y in response:
            return True