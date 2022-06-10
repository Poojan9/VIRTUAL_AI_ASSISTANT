from cgitb import text
from fnmatch import translate
from unittest import result
import pyttsx3
import speech_recognition as sr
import webbrowser
import wikipedia
import pywhatkit
import os
import pyautogui
import pyjokes
import keyboard
from PyDictionary import PyDictionary as diction
import datetime
from playsound import playsound
from googletrans import Translator 
import requests
from bs4 import BeautifulSoup
from pywikihow import search_wikihow 


Assistant = pyttsx3.init("sapi5")
voices = Assistant.getProperty("voices") 
print(voices)
Assistant.setProperty("voices", voices[2].id)
Assistant.setProperty("rate",170)

# This function is used for speak from assistant

def speak(audio):
    print("    ")
    Assistant.say(audio)
    print(f": {audio}")
    print("   ")
    Assistant.runAndWait()

def takecommand():

    command = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        command.pause_threshold = 1
        audio = command.listen(source)

        try:
            print("Recognizing...")
            query = command.recognize_google(audio, language='en-in')
            print(f"You said:{query}")

        except Exception as Error:
            return 'None'

        return query.lower()

def TaskExe():
    # This function are used for music play name of the music is in our systeam then play and not in systeam then music are play in yutube.
    def music():
        speak("Tell me the name of the song!")
        musicname=takecommand()
        if 'henry' in musicname:
            os.startfile("C:\\PYTHON\\henry.mp3")

        else:
            pywhatkit.playonyt(musicname)

        speak("Your song has been started , enjoy sir!")

    # This function are used for messaging a person are define in code through whatsapp.
    def whatsapp():
        speak("tell me the name of the person!")
        name=takecommand()

        if 'poojan' or 'pujan' in name:
            speak("tell me the message!")
            msg=takecommand()
            speak("tell me the time sir!")
            speak("time in hour!")
            hour=int(takecommand())
            speak("time in minutes!")
            min=int(takecommand())
            pywhatkit.sendwhatmsg("+916352557653",msg,hour,min,30)
            speak("ok sir , sending whatsapp message!")

        elif 'mummy' in name:
            speak("tell me the message!")
            msg=takecommand()
            speak("tell me the time sir!")
            speak("time in hour!")
            hour=int(takecommand())
            speak("time in minutes!")
            min=int(takecommand())
            pywhatkit.sendwhatmsg("+919426461601",msg,hour,min,20)
            speak("ok sir , sending whatsapp message!")

    # This function are used for open app in any where in our systeam and not on systeam.
    def openapp():
        speak("ok sir , wait a second")

        if 'spotify' in query:
            os.startfile("C:\\Users\\manthan\\AppData\\Roaming\\Spotify\\Spotify.exe")

        elif 'vlc media player' in query:
            os.startfile("C:\\Program Files\\VideoLAN\\VLC\\vlc.exe")

        elif 'chrome' in query:
            os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")

        elif 'facebook' in query:
            webbrowser.open("https://www.facebook.com/")

        elif 'instagram' in query:
            webbrowser.open("https://www.instagram.com/")

        elif 'maps' in query:
            webbrowser.open("https://www.google.com/maps/@23.0856233,72.6742452,15z")

        elif 'youtube' in query:
            webbrowser.open("https://www.youtube.com/")

        elif 'gmail' in query:
            webbrowser.open("https://gmail.com")
            
        speak("your command has been completed sir!")

    # This function are used for close app in any where in our systeam and not on systeam.
    def closeapp():
        speak("ok sir , wait a second!")

        if 'spotify' in query:
            os.system("TASKKILL /F /im Spotify.exe")

        elif 'vlc media player' in query:
            os.system("TASKKILL /F /im vlc.exe")

        elif 'chrome' in query:
            os.system("TASKKILL /F /im chrome.exe")

        elif 'facebook' in query:
            os.system("TASKKILL /F /im chrome.exe")

        elif 'instagram' in query:
            os.system("TASKKILL /F /im chrome.exe")

        elif 'maps' in query:
            os.system("TASKKILL /F /im chrome.exe")

        elif 'youtube' in query:
            os.system("TASKKILL /F /im chrome.exe")

        elif 'gmail' in query:
            os.system("TASKKILL /F /im chrome.exe")

        speak("your command has been completed!")
 
    # This function can handle Youtube function.
    def youtubeauto():
        speak("Whats your command ?")
        comm=takecommand()

        if 'pause' in comm:
            keyboard.press('space bar')

        elif 'restart' in comm:
            keyboard.press('0')

        elif 'mute' in comm:
            keyboard.press('m')

        elif 'skip' in comm:
            keyboard.press('l')

        elif 'back' in comm:
            keyboard.press('j')

        elif 'full screen' in comm:
            keyboard.press('f')

        elif 'film mode' in comm:
            keyboard.press('t')

        speak('Done sir')

    # def Takehindi():
    #         command = sr.Recognizer()
    #         with sr.Microphone() as source:
    #             print("Listening...")
    #             command.pause_threshold = 1
    #             audio = command.listen(source)

    #             try:
    #                 print("Recognizing...")
    #                 query = command.recognize_google(audio, language='hi')
    #                 print(f"You said : {query}")

    #             except Exception as Error:
    #                 return "None"

    #             return query.lower()

    # def Tran():
    #     speak("Tell me the line!")
    #     line=Takehindi()
    #     traslate=Translator()
    #     result=traslate.translate(line)
    #     Text=result.text
    #     speak(Text)

    # This function can handle Chrome function.
    def chromeauto():

        speak("chrome automation started!")

        command=takecommand()

        if 'close this tab' in command:
            keyboard.press_and_release('ctrl+w')

        elif 'open new tab' in command:
            keyboard.press_and_release('ctrl+t')

        elif 'open new window' in command:
            keyboard.press_and_release('ctrl+n')

        elif 'history' in command:
            keyboard.press_and_release('ctrl+h')
        
    # def dict():
    #     speak("Activated Dictionary")
    #     speak("tell me the problem!")
    #     prob=takecommand()

    #     if 'meaning'in prob:
    #         prob=prob.replace("what is the","")
    #         prob=prob.replace("henry","")
    #         prob=prob.replace("of","")
    #         prob=prob.replace("meaning","")
    #         result=diction.meaning(prob)
    #         speak(f"The meaning for {prob} is {result}")
            
    #     speak("exited dictionary!")

    # This function can take a screenshort of the current window and save in the screenshort folder and then open it.
    def screenshort():
        speak("ok boss , what should i name that file ?")
        path=takecommand()
        path1name=path + ".jpg"
        path1="C:\\Users\\manthan\\Pictures\\Screenshots"+ path1name
        kk=pyautogui.screenshot()
        kk.save(path1)
        os.startfile("C:\\Users\\manthan\\Pictures")
        speak("Here is your screenshort")

    # This function shows us a temprature in any location
    def temp():
        search=takecommand()
        url="https://www.google.com/search?q=" + search
        r=requests.get(url)
        data=BeautifulSoup(r.text,"html.parser")
        temprature=data.find("div",class_="BNeawe").text
        speak(f"The Temprature outside is {temprature} ")

    # This function can check uploading speed , downloading speed and both speed are printed in internet speed .
    def speedtest():
        import speedtest
        speak("Checking speed......")
        speed=speedtest.Speedtest()
        downloading=speed.download()
        correctDown=int(downloading/800000)
        uploading=speed.upload()
        correctUpload=int(uploading/800000)

        if 'uploading' in query:
            speak(f"The uploading speed is {correctUpload} m b p s")

        elif 'downloading' in query:
            speak(f"The Downloading speed is {correctDown} m b p s")

        else:
            speak(f"The Downloading is {correctDown} m b p s and the uploading speed is {correctUpload} m b p s")

    while True:
        # This query command has been defined in while function because this command run for infinity time for taking command from user
    
        query=takecommand()
        if 'hello' in query:
            speak("Hello sir , I Am henry.")
            speak(" Your Personal AI Assistant.")
            speak("How May I Help You ?")

        elif 'how are you' in query:
            speak("I am Fine Sir!")
            speak("Whats About You ?")

        elif 'i am also fine' in query:
            speak("ok Sir!")

        elif 'you need a break' in query:
            speak("ok sir , You Can Call Me Any Time But Now I am Go Bbye.  ")

        elif 'bye' in query:
            speak("ok sir good bye")

        elif 'youtube search' in query:
            speak("Ok Sir , This Is What I Found For Your Search")
            query=query.replace("henry","")
            query=query.replace("youtube search","")
            # query=query.replace("search","")
            web="https://www.youtube.com/results?search_query="+query
            webbrowser.open(web)
            speak("Done Sir!")

        elif 'google search' in query:
            speak("Ok Sir , This Is What I Found For Your Search")
            query=query.replace("henry","")
            query=query.replace("google search","")
            pywhatkit.search(query)
            speak("Done sir!")

        elif 'open website' in query:

            speak("Tell Me The Name Of The Website!")
            name =takecommand()
            web = 'https://www.' + name + '.com'
            webbrowser.open(web)
            speak("Done Sir!")

        elif 'music' in query:
            music()

        elif 'wikipedia' in query:

            speak("searching wikipedia.....")
            query=query.replace("henry","")
            query=query.replace("wikipedia","")
            wiki=wikipedia.summary(query,2)
            speak(f"According to wikipedia :{wiki}")

        elif 'whatsapp message' in query:
            whatsapp()

        elif 'screenshot' in query:
            screenshort()

        elif  'open facebook' in query:
            openapp()

        elif 'open instagram' in query:
            openapp()

        elif 'open maps' in query:
            openapp()

        elif 'open chrome' in query:
            openapp()

        elif 'open gmail' in query:
            openapp()

        elif 'open vlc media player' in query:
            openapp()

        elif 'open spotify' in query:
            openapp()

        elif  'close facebook' in query:
            closeapp()

        elif 'close instagram' in query:
            closeapp()

        elif 'close maps' in query:
            closeapp()

        elif 'close chrome' in query:
            closeapp()

        elif 'close gmail' in query:
            closeapp()

        elif 'close vlc media player' in query:
            closeapp()

        elif 'close spotify' in query:
            closeapp()

        elif 'pause' in query:
            keyboard.press('space bar')

        elif 'restart' in query:
            keyboard.press('0')

        elif 'mute' in query:
            keyboard.press('m')

        elif 'skip' in query:
            keyboard.press('l')

        elif 'back' in query:
            keyboard.press('j')

        elif 'full screen' in query:
            keyboard.press('f')

        elif 'film mode' in query:
            keyboard.press('t')

        elif 'youtube tool' in query:
            youtubeauto()        

        elif 'close the tab' in query:
            keyboard.press_and_release('ctrl+w')

        elif 'open new tab' in query:
            keyboard.press_and_release('ctrl+t')

        elif 'open new window' in query:
            keyboard.press_and_release('ctrl+n')

        elif 'history' in query:
            keyboard.press_and_release('ctrl+h')

        elif 'chrome automation' in query:
            chromeauto()

        elif 'tell me the joke ' in query:
            get = pyjokes.get_joke()
            speak(get)

        elif 'repeat my word' in query:
            speak("speak sir!")
            jj=takecommand()
            speak(f"you said :{jj}")

        # elif 'dictionary' in query:
        #     dict()

        elif 'alarm' in query:
            speak("Enter the time!")
            time=input(":Enter the time:")

            while True:
                time_ac=datetime.datetime.now()
                now = time_ac.strftime("%H:%M:%S")

                if now == time:
                    speak("Time to wake up sir!")
                    os.startfile("C:\\PYTHON\\henry.mp3")
                    speak("Alarm closed!")

                elif now>time:
                    break


        # elif 'translator' in query:
        #     Tran()

        elif "temperature" in query:
            
            speak("Plz tell me name of the city!")
            temp()

        elif 'downloading speed ' in query:
            speedtest()

        elif 'uploading speed' in query:
            speedtest()

        elif 'internet speed' in query:
            speedtest()

        elif 'how to' in query:
            speak("Getting data from the internet !")
            op=query.replace("jarvis","")
            max_result=1
            how_to_func=search_wikihow(op,max_result)
            assert len(how_to_func) == 1
            how_to_func[0].print()
            speak(how_to_func[0].summary)

TaskExe()
        





