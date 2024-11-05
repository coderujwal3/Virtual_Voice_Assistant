import speech_recognition as sr 
import datetime 
import pyttsx3
import sketchpy
import wikipedia 
import webbrowser 
import pyaudio 
import os
import pyautogui
import pyjokes
import random
import AppOpener 
import time
import turtle
from getpass import getpass

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 160)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def WishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning sir!")

    elif hour>=12 and hour<16:
        speak("Good Afternoon sir!")

    else:
        speak("Good Evening sir!")
        
    speak("This is an AI Assistant, Tell me what can I do for you ?")

    
def takeCommand():
    # it takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone(device_index=1) as source:
        print("Listening...")
        r.energy_threshold = 700
        r.pause_threshold = 2
        audio = r.listen(source)

    try:
        print("recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said:, {query}\n")
    except Exception as e:
        print(e)
        print("Not able to hear you sir, please try again...")
        speak("Not able to hear you sir, Please try again...")
        return "None"
    return query.lower()


def TaskExe():

    WishMe()

    def screenshot():
        speak("Ok sir, what should I Name that file")
        name = takeCommand()
        if not name:
            speak("Invalid file name. Please provide a valid name.")
            return
        path1name = name + ".png"
        path1 = ("E:\\screenshots\\") + path1name
        screenshot = pyautogui.screenshot()
        screenshot.save(path1)
        # os.startfile("E:\\screenshots\\")
        speak(f"Here is your Screenshot {path1}")

    def dice_simulator():
        while True:
            print('''1. roll the dice     2. exit    ''')
            user = int(input("what you want to do\n"))
            if user ==1:
                number = random.randint(1,6)
                print(number)
            else:
                break
            
    def password():
        query = speak("tell me the length of password")
        passlen = int(input("enter the length of password"))
        s = "abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#?'*-_+=&"
        p = "".join(random.sample(s,passlen))
        speak("as per your command sir, the code is printed")
        speak(p)
        print(p)

    def cool():
        speak('making cool graphic sir...')
        tu = turtle.Turtle()
        tu.screen.bgcolor("white")
        tu.speed(0)
        tu.shape("arrow")
        tu.shapesize(1.2)
        for i in range(300):
            tu.color('red')
            tu.circle(i)
            tu.color('gold')
            tu.circle(i*0.8)
            tu.right(3)
            tu.forward(3)
        turtle.done()

    def virus():
        speak("ok sir, just a second...")
        tu = turtle.Turtle()
        tu.shape("turtle")
        tu.turtlesize(1.3)
        tu.speed(0)
        tu.color('cyan')
        tu.screen.bgcolor('black')
        b = 200
        while b>0:
            tu.left(b)
            tu.forward(b * 3)
            b = b-1
        tu.hideturtle()
        turtle.done()

    def hide_pass():
        user = input("Username : ")
        password = getpass("Password : ")
        print(user, password)
        
    while True:
        query = takeCommand()

        if 'hello' in query:
            speak("Hello sir , This is Alisha. How may I help you ?")
        
        elif 'tell me your functions' in query:
            speak('''i can do : doing normal conversations, suggest strong password, rolling dice game, pranks like are you online & i love you, making amazing graphics, showing security of passwords, youtube search,
            google search, website, wikipedia, i can open youtube, instagram, gaana, playing song, location, jokes, send gmail to anyone, draw tony, draw image of anyone :  
            Ujwal sir made this AI program.''')

        elif 'how are you' in query:
            speak("You make me always Great sir, what's about you sir!")

        elif 'fine' in query:
            speak("That's awesome, So what I have to do ")

        elif 'suggest me a strong password' in query:
            password()

        elif 'roll the dice' in query:
            speak("Rolling sir")
            time.sleep(1)
            speak("rolled sir...")
            dice_simulator()
        
        elif 'what is your name' in query:
            speak("I am Alisha, an Artificial Voice Assistant made by Ujwal Singh.")

        elif "let's do prank 2" in query:
            prank2()

        elif "cool graphic" in query:
            cool()

        elif 'show the security of password' in query:
            speak("Actually sir, the security is not much secure now, we have to fix it. let's try it once as your command... sir !")
            hide_pass()

        elif 'i am feeling very alone' in query:
            speak("Don't worry sir, i m always with you, you can call me at any time when you need me. I love you sir, i am never going to leave you.")

        elif 'YouTube search' in query:
            speak("Ok sir, This is what you want from me!")
            query = query.replace("youtube search", "")
            web = "https://www.youtube.com/results?search_query=kaushik+shreshth" + query
            webbrowser.open(web) 
            speak("Done sir!")

        elif 'google search' in query:
            speak("This is what I found for your search sir!")
            query = query.replace("Jarvis", "")
            query = query.replace("google search", "")
            pywhatkit.search(query)
            speak("Done sir!")

        elif 'website' in query:
            speak("Ok sir, launching...")
            query = query.replace("Jarvis", "")
            query = query.replace("website", "")
            web1 = query.replace("open", "")
            web2 = "https://www.upsconline.nic" + web1 + ".in"
            webbrowser.open(web2)
            speak("launched!")

        elif 'instagram' in query:
            speak("Ok sir, opening...")
            webbrowser.open("https://www.instagram.com")
            speak("Done sir...")
            print("Done Sir...")

        elif 'Youtube' in query:
            speak("Ok sir, opening...")
            webbrowser.open("https://www.youtube.com")
            speak("Done sir...")

        elif 'gana' in query:
            speak("Ok sir, opening...")
            webbrowser.open("https://www.gaana.com")
            speak("Enjoy it  sir...!")

        elif 'wikipedia' in query:
            speak("searching wikipedia... Please Wait")
            query = query.replace("Jarvis", "")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query , sentences = 10)
            speak("According to Wikipedia...")
            print(results)
            speak(results)
        
        # elif 'open music' in query:
        #     speak("opening your music sir...")
        #     from playsound import playsound
        #     playsound("C:\\Users\\Asus\\Desktop\\Music\\dil bechara.mp3")
        
        # elif 'man meri jaan' in query:
        #     speak("ok sir, wait a while...")
        #     from playsound import playsound
        #     playsound("C:\\Users\\Asus\\Desktop\\Music\\maan meri jaan.mp3")
        #     speak("I hope you are feeling a little bit well now")

        elif 'tell me some jokes' in query:
            get = pyjokes.get_joke(language='en' , category='all')
            print(get)
            speak(get)

        elif 'my location' in query:
            speak("Ok sir, wait a while")
            webbrowser.open("https://www.google.com/maps/@25.284809770741465,82.79121523118496,15z")

        elif 'draw tony' in query:
            from sketchpy import library as lib
            speak("ok sir!")
            time.sleep(0.5)
            obj = lib.rdj()
            speak("Done sir..., the image is drawing.")
            obj.draw()

        elif 'draw spiderman' in query:
            from sketchpy import library as lib
            speak("ok sir!")
            time.sleep(0.5)
            obj = lib.tom_holland()
            speak("Done sir..., the image is drawing.")
            obj.draw()

        elif 'draw image' in query:
            from sketchpy import canvas
            speak("Just a Second sir...")
            obj = canvas.sketch_from_image("E:\IMG_20221118_115550_994.jpg")
            speak("Done sir..., The image is loading !")
            obj.draw()

        elif 'draw coronavirus' in query:
            virus()

        elif 'can you draw my face' in query:
            from sketchpy import canvas
            speak("Why not sir, I am drawing my favourite picture of yours, so be ready to see it.")
            speak("Are you ready sir? , Here you go...")
            obj = canvas.sketch_from_image("E:\\pri\\IMG_20230721_224413_592.jpg")
            speak("Done sir")
            obj.draw()

        elif 'thank you' in query:
            speak("Your most Welcome sir")

        elif 'good' in query:
            speak("Thank You So Much sir!")
        
        elif 'exit' in query: 
            speak("Ok sir, You can call me at anytime, Have a good day sir.")
            break
        
TaskExe()