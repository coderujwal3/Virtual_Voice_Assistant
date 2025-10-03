# alisha_assistant.py
import speech_recognition as sr
import datetime
import pyttsx3
import wikipedia
import webbrowser
import os
import pyautogui
import pyjokes
import random
import time
import threading
from getpass import getpass
from urllib.parse import quote

# Optional imports that may fail (handle gracefully)
try:
    import pywhatkit
except Exception:
    pywhatkit = None

try:
    from sketchpy import library as sketchlib
    from sketchpy import canvas as sketchcanvas
except Exception:
    sketchlib = None
    sketchcanvas = None

# --- Text-to-speech setup ---
def speak(text: str):
    """Speak text and also print to console for debug."""
    if not text:
        return
    print("[ALISHA]:", text)
    try:
        engine = pyttsx3.init('sapi5' if os.name == 'nt' else None)
        voices = engine.getProperty('voices')
        if voices:
            engine.setProperty('voice', voices[1].id)
        engine.setProperty('rate', 160)
        engine.say(text)
        engine.runAndWait()
        engine.stop()
    except Exception as e:
        print("TTS Error:", e)


# --- Recognition helpers ---
recognizer = sr.Recognizer()

def take_command(timeout=5, phrase_time_limit=8):
    """
    Attempt to capture a voice command. If speech recognition fails, fall back to keyboard input.
    Returns lowercased string.
    """
    with sr.Microphone() as source:
        try:
            # Calibrate for ambient noise for 0.5 seconds
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            # speak("Listening...")
            audio = recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
            # speak("Recognizing...")
            query = recognizer.recognize_google(audio, language='en-in')
            print("Boss command:", query)
            return query.lower()
        except sr.WaitTimeoutError:
            print("No speech heard (timeout).")
            speak("I couldn't hear anything. You can type your command if you prefer.")
        except sr.UnknownValueError:
            print("Could not understand audio.")
            speak("Sorry, I didn't catch that.")
        except sr.RequestError as e:
            print("SR Request Error:", e)
            speak("Speech service is unavailable right now.")

    # Fallback to keyboard input - if no query understandable
    try:
        fallback = input("Type your command (or press Enter to skip): ").strip()
        return fallback.lower() if fallback else "none"
    except Exception:
        return "none"


# --- Utility functions ---
def wish_me():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good Morning Sir!")
    elif 12 <= hour < 16:
        speak("Good Afternoon Sir!")
    else:
        speak("Good Evening Sir!")
    speak("This is Alisha, your virtual voice Assistant. Tell me what I can do for you.")


# Create screenshots folder if not present
DEFAULT_SCREENSHOT_DIR = os.path.join(os.path.expanduser("~"), "Alisha_Screenshots")
os.makedirs(DEFAULT_SCREENSHOT_DIR, exist_ok=True)


def take_screenshot():
    speak("What should I name the screenshot? Say the name or type it.")
    name = take_command()
    if not name or name == "none":
        # keyboard input 
        name = input("Enter screenshot name (without extension): ").strip() or f"screenshot_{int(time.time())}"
    filename = f"{name}.png"
    path = os.path.join(DEFAULT_SCREENSHOT_DIR, filename)
    try:
        img = pyautogui.screenshot()
        img.save(path)
        speak(f"Screenshot saved to {path}")
    except Exception as e:
        speak("Failed to take screenshot.")
        print("Screenshot error:", e)


def dice_simulator():
    speak("Dice simulator started. Say 'roll' to roll the dice or 'exit' to stop.")
    while True:
        cmd = take_command()
        if 'roll' in cmd:
            number = random.randint(1, 6)
            speak(f"You rolled a {number}")
            print("Rolled:", number)
        elif 'exit' in cmd or cmd == 'none':
            speak("Exiting dice simulator.")
            break
        else:
            speak("Say 'roll' or 'exit'.")


def generate_password():
    speak("Tell me the length of the password you want.")
    cmd = take_command()
    try:
        length = int(cmd)
    except Exception:
        try:
            length = int(input("Enter password length (e.g. 12): ").strip())
        except Exception:
            length = 12 # default length will be 12

    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#?'*-_+=&"
    password = "".join(random.sample(chars, min(length, len(chars))))
    speak("Here is your password. I will display it on screen as well.")
    print("Generated password:", password)


def hide_pass():
    user = input("Username: ")
    password = getpass("Password: ")
    print("Credentials (printed for demo):", user, password)
    speak("Credentials captured (check your console).")

# To draw using Turtle
def run_in_thread(fn, *args, **kwargs):
    t = threading.Thread(target=fn, args=args, kwargs=kwargs, daemon=True)
    t.start()
    return t


def cool_graphic():
    import turtle as t
    def draw():
        try:
            tu = t.Turtle()
            screen = t.Screen()
            screen.bgcolor("white")
            tu.speed(0)
            tu.shape("arrow")
            tu.shapesize(1.2)
            for i in range(300):
                tu.color('red')
                tu.circle(i)
                tu.color('gold')
                tu.circle(int(i*0.8))
                tu.right(3)
                tu.forward(3)
            t.done()
        except Exception as e:
            print("Turtle error:", e)
            speak("Failed to draw the graphic.")
    run_in_thread(draw)


def virus_graphic():
    import turtle as t
    def draw():
        try:
            tu = t.Turtle()
            screen = t.Screen()
            screen.bgcolor('black')
            tu.shape("turtle")
            tu.turtlesize(1.3)
            tu.speed(0)
            tu.color('cyan')
            b = 200
            while b > 0:
                tu.left(b)
                tu.forward(b * 3)
                b -= 1
            tu.hideturtle()
            t.done()
        except Exception as e:
            print("Turtle error:", e)
            speak("Failed to draw the virus graphic.")
    run_in_thread(draw)


# prank function
def prank_typewriter():
    speak("Initiating harmless prank: typewriter effect in console.")
    message = "Are you online?"
    for ch in message:
        print(ch, end="", flush=True)
        time.sleep(0.12)
    print()
    speak("Prank finished.")


# --- Sketchpy functions ---
def draw_rdj():
    if not sketchlib:
        speak("Sketch functionality is not available. sketchpy is not installed.")
        return
    speak("Drawing RDJ. This may take a few seconds.")
    try:
        obj = sketchlib.rdj()
        # run draw in thread to avoid blocking
        run_in_thread(obj.draw)
    except Exception as e:
        print("sketchpy error:", e)
        speak("Failed to draw using sketchpy.")


def draw_tom_holland():
    if not sketchlib:
        speak("Sketch functionality is not available.")
        return
    speak("Drawing Spiderman (Tom Holland).")
    try:
        obj = sketchlib.tom_holland()
        run_in_thread(obj.draw)
    except Exception as e:
        print("sketchpy error:", e)
        speak("Failed to draw using sketchpy.")


def sketch_from_image(path):
    if not sketchcanvas:
        speak("Sketch from image not available. sketchpy not installed.")
        return
    if not os.path.exists(path):
        speak(f"The image path {path} does not exist.")
        return
    speak("Sketching the provided image. This might take a moment.")
    try:
        obj = sketchcanvas.sketch_from_image(path)
        run_in_thread(obj.draw)
    except Exception as e:
        print("sketchpy canvas error:", e)
        speak("Failed to sketch the image.")


# --- Main execution loop ---
def main_loop():
    wish_me()
    while True:
        query = take_command()
        if not query or query == "none":
            continue

        # Basic interactions
        if 'hello' in query or 'hi' in query:
            speak("Hello sir, my name is Alisha. How may I help you?")
        elif 'how are you' in query:
            speak("I'm fine, thank you. How are you?")
        elif 'fine' in query:
            speak("That's great. What can I do for you?")
        elif 'thank you' in query:
            speak("You're most welcome.")
        elif 'exit' in query or 'quit' in query or 'stop' in query:
            speak("Ok sir, you can call me anytime. Have a good day!")
            break

        # Utilities
        elif 'screenshot' in query or 'screen shot' in query:
            take_screenshot()

        elif 'roll the dice' in query or 'roll dice' in query or 'roll' == query.strip():
            dice_simulator()

        elif 'suggest a strong password' in query or 'strong password' in query:
            generate_password()

        elif 'show the security of password' in query or 'check password' in query:
            hide_pass()

        elif 'prank' in query:
            prank_typewriter()

        elif 'cool graphic' in query:
            cool_graphic()

        elif 'draw coronavirus' in query or 'virus' in query:
            virus_graphic()

        # Web and search
        elif 'youtube' in query and 'search' in query:
            # Example: "youtube search classical music"
            speak("Searching YouTube for you.")
            term = query.replace("youtube search", "").strip()
            if not term:
                speak("Please tell me what to search on YouTube.")
                term = take_command()
            if term and term != 'none':
                url = "https://www.youtube.com/results?search_query=" + quote(term)
                webbrowser.open(url)
                speak("Opened YouTube search results.")
            else:
                speak("No search term provided.")

        elif 'youtube' in query and 'open' in query:
            speak("Opening YouTube.")
            webbrowser.open("https://www.youtube.com")

        elif 'google search' in query or ('search' in query and 'google' in query):
            speak("Searching on Google.")
            term = query
            # strip trigger words
            for token in ["google search", "alisha", "search"]:
                term = term.replace(token, "")
            term = term.strip()
            if not term:
                speak("What should I search for?")
                term = take_command()
            if pywhatkit and term and term != 'none':
                try:
                    pywhatkit.search(term)
                    speak("Here are the search results.")
                except Exception:
                    # fallback to webbrowser
                    webbrowser.open("https://www.google.com/search?q=" + quote(term))
                    speak("Opened Google results in your browser.")
            elif term and term != 'none':
                webbrowser.open("https://www.google.com/search?q=" + quote(term))
                speak("Opened Google results in your browser.")
            else:
                speak("No search term provided.")

        elif 'open website' in query or 'open' in query and 'website' in query:
            speak("Which website should I open? Say the domain or full URL.")
            site = take_command()
            if site and site != 'none':
                if not site.startswith("http"):
                    if '.' in site:
                        url = "https://" + site
                    else:
                        url = "https://www." + site + ".com"
                else:
                    url = site
                try:
                    webbrowser.open(url)
                    speak(f"Opened {url}")
                except Exception:
                    speak("Couldn't open that website.")
            else:
                speak("No website provided.")

        elif 'instagram' in query:
            speak("Opening Instagram.")
            webbrowser.open("https://www.instagram.com")

        elif 'gana' in query or 'gaana' in query or 'music' in query:
            speak("Opening Gaana.")
            webbrowser.open("https://www.gaana.com")

        elif 'wikipedia' in query:
            speak("Searching Wikipedia. Tell me the topic.")
            topic = query.replace("wikipedia", "").strip()
            if not topic:
                topic = take_command()
            if topic and topic != 'none':
                try:
                    results = wikipedia.summary(topic, sentences=3)
                    speak("According to Wikipedia:")
                    print(results)
                    speak(results)
                except Exception as e:
                    print("Wikipedia error:", e)
                    speak("I couldn't find a summary for that topic.")
            else:
                speak("No topic provided.")

        elif 'tell me some jokes' in query or 'joke' in query:
            try:
                joke = pyjokes.get_joke()
                speak(joke)
            except Exception:
                speak("I couldn't get a joke right now.")

        elif 'my location' in query or 'where am i' in query:
            speak("Opening Google Maps for your approximate location.")
            # Replace this with coordinates if you'd like dynamic location lookup
            webbrowser.open("https://www.google.com/maps")

        # Sketchpy drawing commands
        elif 'draw tony' in query or 'draw rdj' in query:
            draw_rdj()

        elif 'draw spiderman' in query or 'draw tom holland' in query:
            draw_tom_holland()

        elif 'draw image' in query or 'draw my face' in query:
            speak("Please provide the full image path (type it here).")
            path = input("Enter image path: ").strip()
            if path:
                sketch_from_image(path)
            else:
                speak("No image path provided.")

        else:
            # If nothing matched, offer a fallback to search
            speak("I did not understand that. Do you want me to search the web for it? Say 'yes' to search.")
            yn = take_command()
            if 'yes' in yn or 'yeah' in yn:
                # re-use google search flow
                term = query
                webbrowser.open("https://www.google.com/search?q=" + quote(term))
                speak("Opened web search for your query.")


if __name__ == "__main__":
    try:
        main_loop()
    except KeyboardInterrupt:
        speak("Shutting down. Goodbye.")
    except Exception as e:
        print("Fatal error:", e)
        speak("An unexpected error occurred. Check the console for details.")
