'''r'F:\Documents\Python scripts\spiral-design-animation.gif'''
import tkinter
from PIL import Image, ImageTk, ImageSequence
import pyttsx3
from threading import *
from time import sleep
import speech_recognition as sr
import os
import subprocess
import webbrowser
import sys


root = tkinter.Tk()
engine = pyttsx3.init()
r = sr.Recognizer()
text=""
class JarvisUI(Thread):
    def run(self):
        class App():
            def __init__(self, parent):
                self.parent = parent
                self.canvas = tkinter.Canvas(parent, width=400, height=400)
                self.canvas.pack()
                self.sequence = [ImageTk.PhotoImage(img)
                                    for img in ImageSequence.Iterator(
                                            Image.open('jarvis.gif'
                                            ))]
                self.image = self.canvas.create_image(200,200, image=self.sequence[0])
                self.animate(1)

            def animate(self, counter):
                self.canvas.itemconfig(self.image, image=self.sequence[counter])
                self.parent.after(20, lambda: self.animate((counter+1) % len(self.sequence)))
        global root
        root.title("Jarvis")
        root.resizable(False,False)
        app = App(root)
        

class Speech(Thread):
    def run(self):
        speech_text=""
        global engine
        engine.say("Hi Sir Jarvis is there at your service sir")
        engine.say("What can i do for you")
        engine.runAndWait()
        while(1):
            speech_text=recognize()
            if(speech_text==None):
                speech_text=""
            print(speech_text)
            #sleep(1)
            if(speech_text=="log off"):
                engine.say("logging off")
                engine.runAndWait()
                os.system("shutdown -l")
            elif(speech_text=="notepad"):
                engine.say("opening notepad")
                engine.runAndWait()
                os.system("start notepad.exe")
                #repeat()
            elif(speech_text=="close"):
                engine.say("Have a nice day sir")
                engine.runAndWait()
                on_closing()
                break
            elif(speech_text=="Chrome"):
                engine.say("opening chrome")
                engine.runAndWait()
                os.system("start chrome.exe")
                #repeat()
            elif(speech_text=="music"):
                webbrowser.open('https://www.youtube.com/watch?v=Az-mGR-CehY&list=PL0WXNHQ4HAfaSXr_lzVY9dzIz5g7Tybkv&index=6&t=0s&ab_channel=K-391')
                
                #repeat()
            else:
                if(len(str(speech_text))!=0):
                    print(speech_text)
                    engine.say("Sorry, I did not get that")
                    engine.runAndWait()
                root.protocol("WM_DELETE_WINDOW",on_closing)
                #repeat()
                
      
        

def on_closing():
    root.destroy()
    sys.exit()

def stop(self): 
    self._is_running = False


            
def recognize():
    global engine
    global r
    global text
    # Initialize recognizer class (for recognizing the speech)

    #r = sr.Recognizer()
    
    # Reading Microphone as source
    # listening the speech and store in audio_text variable
    with sr.Microphone() as source:
        engine.say("Please Speak")
        engine.runAndWait()
        #r.adjust_for_ambient_noise(source)
        audio_text = r.listen(source)
        #print(audio_text)
        #print("Time over, thanks")
        
    # recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
        try:
            # using google speech recognition
            print("Text: "+r.recognize_google(audio_text))
            text=r.recognize_google(audio_text)
            return text
        except Exception as e:
            print("Value")
            print(e)
            if(text==None):
                text=""
            if(len(text)!=0): 
                engine.say("Sorry speak it again")
                engine.runAndWait()
                print("Sorry, I did not get that")
    
    
def listen():
    thread1=JarvisUI()
    thread2=Speech()
    #reg_text=recognize()
    reg_text="Jarvis"
    if(reg_text=="Jarvis"):
        thread1.start()
        sleep(0.2)
        thread2.start()
        
        root.mainloop()
    else:
        print("Speak again")
        listen()
 
        
listen()
