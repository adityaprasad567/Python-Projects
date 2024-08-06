import speech_recognition as sr
import webbrowser
import pyttsx3
import requests
import openai
import pygame
import os
from gtts import gTTS
import openai

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "20036166c6f2410b84e894e1a59b8f68"

def speak_old(text):
    engine.say(text)
    engine.runAndWait()

def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3')
    
    # Initialize Pygame mixer
    pygame.mixer.init()

    # Load the MP3 file
    pygame.mixer.music.load('temp.mp3')

    # Play the MP3 file
    pygame.mixer.music.play()

    # Keep the program running until the music stops playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    
    pygame.mixer.music.unload()
    os.remove("temp.mp3")

def aiProcess(command):
    openai.api_key = "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"

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a virtual assistant named Jarvis skilled in general tasks like Alexa and Google Cloud. Give short responses please."},
            {"role": "user", "content": command}
        ]
    )

    return response.choices[0].message['content']

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("http://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("http://youtube.com")
    elif "open amazon" in c.lower():
        webbrowser.open("http://amazon.in")
    elif "temperature" in query:
                    search = "temperature in delhi"
                    url = f"https://www.google.com/search?q={search}"
                    r  = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current{search} is {temp}")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
    elif "what is your name" in c.lower():
        speak("My name is Peter")
    elif "How are you" in c.lower():
        speak("Im fine Sir, whats about you sir")
    elif "what time is it" in c.lower():
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        speak(f"The current time is {current_time}")
    elif "who is your favorite hero" in c.lower():
        speak("my favorite hero one only allu arjun as it is my boss favorite")
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code == 200:
            # Parse the JSON response
            data = r.json()
            
            # Extract the articles
            articles = data.get('articles', [])
            
            # Speak the headlines
            for article in articles:
                speak(article['title'])
    else: #pass
        # Let OpenAI handle the requests
        output = "i dont know"
        speak(output)
        
    #print(c)

if __name__ == '__main__':
    speak("Initializing Peter...")
    while True:
        try:
            with sr.Microphone() as source:
                print("Listening for wake word...")
                audio = recognizer.listen(source, timeout=2, phrase_time_limit=1)
                word = recognizer.recognize_google(audio)
                
            if word.lower() == "peter":
                speak("Yes Sir")
                
                with sr.Microphone() as source:
                    print("Peter Active...")
                    audio = recognizer.listen(source)
                    command = recognizer.recognize_google(audio)
                    processCommand(command)
                    
        except Exception as e:
            print("Error: {0}".format(e))
