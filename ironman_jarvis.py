import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import pyaudio
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Jarvis Sir. Please tell me how may I help you")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone(device_index=1) as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('kumardeepak96162@gmail.com', 'deepak1234a')
    server.sendmail('kumardeepak96162@gmail.com', to, content)
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

        elif 'open youtube' in query or "youtube" in query:
            webbrowser.open("https://www.youtube.com")
            speak("opening youtube")

        elif 'open google' in query or "google" in query:
            webbrowser.open("https://www.google.com")
            speak("opening google")

        elif 'open snapdeal' in query or "snapdeal" in query:
            webbrowser.open("https://www.snapdeal.com")
            speak("opening snapdeal")

        elif 'open amazon' in query or 'shop online' in query or "amazon" in query:
            webbrowser.open("https://www.amazon.com")
            speak("opening amazon")

        elif 'open yahoo' in query or "yahoo" in query:
            webbrowser.open("https://www.yahoo.com")
            speak("opening yahoo")

        elif 'open gmail' in query or "gmail" in query:
            webbrowser.open("https://mail.google.com")
            speak("opening google mail")

        elif 'open stack overflow' in query or "stack overflow" in query:
            webbrowser.open("https://www.stackoverflow.com")
            speak("opening stackoverflow")

        elif 'open facebook' in query or "facebook" in query:
            webbrowser.open("https://www.facebook.com")
            speak("opening facebook")

        elif 'open flipkart' in query:
            webbrowser.open("https://www.flipkart.com")
            speak("opening flipkart")

        elif 'make you' in query or 'created you' in query or 'develop you' in query:
            ans_m = " For your information Deepak Kumar created me ! I give Lot of Thannks to Him "
            print(ans_m)
            speak(ans_m)

        elif "who are you" in query or "about you" in query or "your details" in query:
            about = "I am Jarvis an A I based computer program but i can help you lot like a your close friend ! i promise you ! Simple try me to give simple command ! like playing music or video from your directory i also play video and song from web or online ! i can also entain you i so think you Understand me ! ok Lets Start "
            print(about)
            speak(about)

        elif "your name" in query or "sweat name" in query:
            na_me = "Thanks for Asking my name my self ! Jarvis"
            print(na_me)
            speak(na_me)

        elif "your feeling" in query or "feeling" in query:
            print("feeling Very sweet after meeting with you")
            speak("feeling Very sweet after meeting with you")


        elif 'play music' in query or "music" in query:
            music_dir = 'F:\\music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'video from pc' in query or "video" in query:
            speak("ok i am playing videos")
            video_dir = 'F:\\videos\\wedding 2'
            videos = os.listdir(video_dir)
            os.startfile(os.path.join(video_dir, videos[0]))

        elif 'goodbye' in query:
            speak("good bye")
            exit()

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\DEEPAK KUMAR\\Anaconda3\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email to roop' in query or "send email" in query or "email" in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = ["imroopkishor@gmail.com","gangwardeepak698@gmail.com"]
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend deepak bhai. I am not able to send this email")
