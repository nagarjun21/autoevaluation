import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import pytz

# initialize the text-to-speech engine
engine = pyttsx3.init()

# define a function to speak the given text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# define a function to recognize speech
def recognize_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak now...")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("You said: ", text)
        return text
    except sr.UnknownValueError:
        print("Sorry, I didn't understand what you said.")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

# define a function to process the user's command
def process_command(command):
    if "open Google" in command:
        webbrowser.open("https://www.google.com")
        speak("Opening Google.")
    elif "what's the weather like" in command:
        webbrowser.open("https://www.weather.com")
        speak("Let me check the weather for you.")
    elif "what's the time" in command:
        tz_NY = pytz.timezone('America/New_York') 
        datetime_NY = datetime.datetime.now(tz_NY)
        current_time = datetime_NY.strftime("%I:%M %p")
        speak("The current time is " + current_time + " in New York.")
    elif "open Visual Studio Code" in command:
        speak("Opening Visual Studio Code.")
        codePath = "C:\\Users\\Username\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        webbrowser.open(codePath)
    elif "stop" in command:
        speak("Goodbye!")
        exit()
    else:
        speak("I'm sorry, I don't understand what you're asking for.")

# main program loop
while True:
    speak("How can I help you?")
    command = recognize_speech()
    if command:
        process_command(command)

    