import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random
import subprocess
from sys import exit

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        print(" Nice to meet you, good morning how can i help you ")
        speak(" Nice to meet you, good morning how can i help you ")
    elif hour >= 12 and hour < 18:
        print(" Nice to meet you, GoodAfternoon HowCan I Help You?")
        speak(" Nice to meet you, GoodAfternoon HowCan I Help You?")
    else:
        print("Nice to meet you, good morning how can i help you ")
        speak("Nice to meet you, GoodEvening HowCan I Help You?")


def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.7
        audio = r.listen(source)

    try:
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        return "None"
    return query


def note(text):
    date = datetime.datetime.now()
    file_name = str(date).replace(":", "-") + "-note.txt"
    with open(file_name, "w") as f:
        f.write(text)
    subprocess.Popen(["notepad.exe", file_name])


if __name__ == "__main__":
    dice = random.randint(1, 6)
    wishMe()

    while True:
        query = takeCommand().lower()
        if 'ok tune' in query:
            print("How Can i Help You")
            speak("How can I Help You")
            query = takeCommand().lower()

            if 'wikipedia' in query:
                speak('Searching Wikipedia')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)

            elif 'youtube' in query:
                query = query.replace("youtube search", "")
                query = query.replace("youtube", "")
                yq = "https://www.youtube.com/results?search_query=" + query
                webbrowser.open(yq)

            elif 'open google' in query:
                webbrowser.open("google.com")

            elif 'google kholo' in query:
                webbrowser.open("google.com")

            elif 'weather' in query:
                webbrowser.open("https://www.google.com/search?q=weather&sxsrf=ALiCzsZ1eQifK27JKlpaDrYnJ10bbWitOw%3A1652064904989&source=hp&ei=iIJ4YoOMOuqHr7wP6ouzsAc&iflsig=AJiK0e8AAAAAYniQmExTcEmFW1awv9h9MyHwxhrn2ydo&ved=0ahUKEwiD8LiutdH3AhXqw4sBHerFDHYQ4dUDCAc&uact=5&oq=weather&gs_lcp=Cgdnd3Mtd2l6EAMyEAgAEIAEELEDEIMBEEYQgAIyCwgAEIAEELEDEIMBMg4IABCABBCxAxCDARDJAzIFCAAQkgMyBQgAEJIDMgUIABCABDILCAAQgAQQsQMQgwEyBQgAEIAEMgsIABCABBCxAxCDATIFCAAQsQM6BAgjECc6CwguEIAEELEDEIMBOggIABCxAxCDAToRCC4QgAQQsQMQgwEQxwEQrwE6DgguEIAEELEDEMcBENEDUABYuApg-RFoAHAAeACAAXuIAakGkgEDMC43mAEAoAEB&sclient=gws-wiz")

            elif 'college site' in query:
                webbrowser.open("https://www.shahandanchor.com/home/")

            elif 'note' in query:
                speak("What would you like me to write down? ")
                write_down = query = takeCommand().lower()
                note(write_down)
                speak("I've made a note of that.")

            elif 'music' in query:
                music_dir = 'C:\\Users\\hp\\Music\\Video Projects'
                songs = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir, songs[0]))

            elif 'time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                print(f"The time is {strTime}")
                speak(f"The time is {strTime}")

            elif 'code' in query:
                codePath = "C:\\Users\\hp\\AppData\\Local\\Programs\Microsoft VS Code\\Code.exe"
                os.startfile(codePath)
                print("Opening VS Code")
                speak("Opening VS Code")

            elif 'dice' in query:
                print(dice)
                speak(dice)

            elif 'sleep' in query:
                print("Goodbye have a nice day")
                speak("Goodbye have a nice day")
                exit()

            else:
                print("Sorry didnt get you")
                speak("Sorry didnt get you")
