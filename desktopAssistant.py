import pyttsx3  #This module used to convert text-to-speech
import speech_recognition as sr   #This module used to recognize the human voice and convert into computer language
import datetime
import wikipedia   #This module used to search anything On Wikipedia
import webbrowser   #This module used to open Default web browser in the system 
import os
import smtplib
import time

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[0].id)

chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
        print("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   
        print("Good Afternoon!")
    else:
        speak("Good Evening!")  
        print("Good Evening!")  
    speak("I am sova. Here at your Service.")       
    print("I am sova. Here at your Service.")
    

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        # r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('kuchbhi.kuchbhi2611@gmail.com', 'kuchbhi2611')
    server.sendmail('kuchbhi.kuchbhi2611@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak('Opening YouTube in Chrome...')
            print('Opening YouTube in Chrome...')
            webbrowser.get(chrome_path).open("youtube.com")

        elif 'open google' in query:
            speak('Opening Google in Chrome...')
            print('Opening Google in Chrome...')
            webbrowser.get(chrome_path).open("google.com")

        elif 'open mail' in query:
            speak('Opening gmail in Chrome...')
            print('Opening gmail in Chrome...')
            webbrowser.get(chrome_path).open("gmail.com")

        elif 'open GitHub' in query:
            speak('Opening GitHub in Chrome')
            webbrowser.get(chrome_path).open("GitHub.com")   

        elif 'covid'  in query:
            speak('Showing Live COVID updates in India')
            webbrowser.get(chrome_path).open("mohfw.gov.in/")


        elif 'play music' in query:
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
            print(strTime)

        elif 'email to Zora' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "naman_sharma.scsebtech@galgotiasuniversity.edu.in "    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend. I am not able to send this email")  

           

        elif "don't listen" in query or "stop listening" in query: 
            speak("for how much time you want to stop listening commands") 
            a = int(takeCommand()) 
            time.sleep(a) 
            print(a) 

        elif 'exit' in query: 
            speak("Thanks for giving me your time") 
            exit() 
        
        #else:
        #    speak("Sorry Sir. Please, Say a valid command")
