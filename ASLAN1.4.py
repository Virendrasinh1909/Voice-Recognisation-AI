import pyttsx3
import tkinter as tk
import re
import time
import datetime
import speech_recognition as sr
import mysql.connector
from tkinter import *
from hotword import *
from program import *
from pyttsx3 import *
#------------------------------------------------------DataBase----------------------------------------------------------------
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="@Virendrasinh#1909@",
  database="hotword"
)

#-----------------------------------------------------ClearText----------------------------------------------------------------
def cls():
    textbox.configure(state='normal')
    textbox.delete(1.0, END)
    textbox.configure(state='disabled')
#-----------------------------------------------------Canvas-------------------------------------------------------------------
window = tk.Tk()
window.title("ASLAN")

photo = PhotoImage(file = "C:/Users/New/Desktop/RawData/Speech To Text/ASLAN/ASLAN0.2/logo-1.png")
window.iconphoto(False, photo)

canvas = Canvas(window, width = 600, height = 300)
canvas.pack()

label = tk.Label(window, text="""Click On "Listen" and Say Cammand...""", font=('helvetica', 12))
canvas.create_window(300,20,window=label)

textbox = tk.Text(window, width = 50, height=5)
canvas.create_window(300,100,window=textbox)
textbox.configure(state='normal')
textbox.insert(tk.END,"Say cammand...\n")
textbox.configure(state='disabled')

#-----------------------------------------------------SpeechRecognition--------------------------------------------------------
def stt(event):
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        
        audio = r.listen(source)
        try:
            you_said = r.recognize_google(audio)
        except r.UnknownValueErrors:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
        except Exception as e:
            print("Error : " + str(e))
    
#-----------------------------------------------------PrintInCanvas------------------------------------------------------------    
    textbox.configure(state='normal')
    textbox.insert(tk.END,"You   :" + you_said + "\n") 
    textbox.configure(state='disabled')
    window.update()
#------------------------------------------------------------------------------------------------------------------------------
    try:
        aslan_said = str(hotword(you_said))
    except:
        pass

    try:
        mycursor = mydb.cursor()
        sql = "SELECT aslan_said FROM Hotword WHERE you_said = %s"
        adr = (you_said, )
        mycursor.execute(sql, adr)
        myresult = mycursor.fetchall()
        for x in myresult:
            aslan_said = ''.join(x)
    except:
        pass
    try:
        m = re.match(r"(?P<open>\w+) (?P<program>.*$)", you_said)
        m.group('program')
        if m.group('open') == 'open':
            aslan_said = program(str(m.group('program')))
    except:
        pass
#------------------------------------------------------------------------------------------------------------------------------
    textbox.configure(state='normal')
    textbox.insert(tk.END,"ASLAN :" + aslan_said + "\n")
    textbox.configure(state='disabled')
    time.sleep(1)
    window.update()
#-----------------------------------------------------VoiceReplay--------------------------------------------------------------    
    engine = pyttsx3.init()

    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)    #set voice[0] for men and voice[1] for female

    rate = engine.getProperty('rate')   # getting details of current speaking rate
    engine.setProperty('rate', 150)     # setting up new voice rate

    engine.say(aslan_said)
    engine.runAndWait()

window.bind('<Return>', stt)
listen_button = tk.Button(text='LISTEN', command=lambda:[stt(None)], bg='brown',fg='white')
canvas.create_window(200, 250, window=listen_button)

clear_button = tk.Button(text='CLEAR', command=cls,bg='brown',fg='white')
canvas.create_window(400, 250, window=clear_button)

copy_right = tk.Label(window, text="@ASLAN", fg='gray', font=('arial', 8))
canvas.create_window(550,280,window=copy_right)

window.mainloop()