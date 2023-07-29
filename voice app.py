from tkinter import *
import speech_recognition as sr
import pyttsx3 
import webbrowser
from datetime import datetime
import subprocess

root=Tk()

root.geometry("700x600")
root.title("pro")
root.configure(bg="grey")

HeadName=Label(root,text="Welcome to your desktop assistant",fg="orange",bg="grey",font=("Classic",30,"bold","italic"))        
HeadName.place(relx=0.5,rely=0.2,anchor=CENTER)

text_to_speech=pyttsx3.init

def r_audio ():
    speech_recognizer=sr.Recognizer()
    speak("how can i help you")
    with sr.Microphone() as source:
        audio=speech_recognizer.listen(source)
        voice_data=""
        try:
            voice_data=speech_recognizer.recognize_google(audio,language="en-in")
        except sr.UnknownValueError:
            speak("please repeat i did not get that")
            r_audio()
        respond(voice_data)

def respond (voice_data):
    print(voice_data)

btn=Button(root,text="start",bg="yellow",fg="red",font=("Classic",20,"bold"),command=r_audio)
btn.place(relx=0.5,rely=0.4,anchor=CENTER)

root.mainloop()