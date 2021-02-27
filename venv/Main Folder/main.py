import speech_recognition as sr
from Utilities.partsOfSpeech import POS
import pyttsx3

#declare an object
rec = sr.Recognizer()
pos = POS()
speak = pyttsx3.init()

#enable microphone
with sr.Microphone() as source:

    #remove ambient noise from voice
    rec.adjust_for_ambient_noise(source)
    
    #listen the voice

    speak.say("say a sentence to get parts of speech")
    speak.runAndWait()
    rec.record(source=source, duration=0.1)
    audio = rec.listen(source)
    print("-----Stopped Listening-----")

    try:
        #do voice to text translation
        print("-----Converting voice to text-----")
        text = rec.recognize_google(audio)
        print("You said below words\n{}".format(text)) 
        pos.getPOS(text)
    except sr.UnknownValueError as e:
        print("I couldn't understand audio")
    except sr.RequestError as e:
        print(e)

