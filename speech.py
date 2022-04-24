import speech_recognition as sr
import pyaudio

r = sr.Recognizer()
with sr.Microphone() as source:                         # use the default microphone as the audio source
    print("Speak Anything :")                           
    audio = r.listen(source)                            # listen for the first phrase and extract it into audio data
    try:
        text = r.recognize_google(audio)                # recognize speech using Google Speech Recognition
        print("You said : {}".format(text))
    except LookupError:                                 # speech is unintelligible
        print("Sorry could not recognize your voice")