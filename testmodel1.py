import pyttsx3
import wikipedia
import datetime
import speech_recognition as sr 
import webbrowser
import smtplib
import requests
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

rate = engine.getProperty('rate') 
engine.setProperty('rate', 200)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Boss")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Boss")
    else:
        speak("Good Evening Boss")
        
    speak("My name is Luna")


def playSong():
    play_Song = "D:\\Songs"
    music=os.listdir(play_Song)
    os.startfile(os.path.join(play_Song,music[0]))
    
def get_weather():
    api_key = "cd635cf08c88af3fc464ef834aa526ce"
    BASE_URL="http://api.openweathermap.org/data/2.5/weather?"
    city = "Rajkot"
    url = BASE_URL+"appid="+api_key+"&q="+city

    response = requests.get(url)
    weather_data = response.json()
    
    if response.status_code != 200:
        print("Failed to get weather data. Please check the city name or API key.")
        speak("Failed to get weather data. Please check the city name or API key.")
        return

    if 'name' not in weather_data:
        print("Invalid response structure.")
        speak("Invalid response structure.")
        return

    location = weather_data['name']
    current_temp = weather_data['main']['temp'] - 273.15  # Convert from Kelvin to Celsius
    condition = weather_data['weather'][0]['description']
    print(f"Todays Weather in {location} is {current_temp:.2f}°C with {condition}.")
    speak(f"Todays Weather in {location} is {current_temp:.2f}°C with {condition}.")

def sendEmail(to , content):
     server = smtplib.SMTP('smtp.gmail.com',587)
     server.ehlo()
     server.starttls()
     server.login('aadil.parmar25official@gmail.com','mnvr yjkp btyk myrt')
     server.sendmail('aadil.parmar25official@gmail.com',to,content)
     server.close()
     
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone()as source:
        print("Listing..")
        speak("Give me Order Boss")
        r.pause_threshold=1.5
        r.energy_threshold=100
        audio=r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio, language='en-in')
        print(f"User said : {query}\n")
        
    except Exception as e:
        speak("Can you say that again Boss?")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    get_weather()
    if 1:
        query=takeCommand().lower()

        if 'wikipedia'in query:
            speak("Searching..")
            query=query.replace("wikipedia","")
            results=  wikipedia.summary(query,sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)
          
        if 'stop' in query:
                speak("Okay Boss!")

        elif 'exit' in query:
                speak("Have a good day Boss!")
 
        elif 'open youtube'in query:
                webbrowser.open("youtube.com")

        elif 'open google'in query:
                webbrowser.open("google.com")

        elif 'open tradingview'in query:
                webbrowser.open("tradingview.com")

        elif 'the time'in query:
                strTime=datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Its {strTime} Boss!")   
                
        elif'weather'in query:
            get_weather()
            
        elif'email'in query:
            try:
                speak("what shoul I say Boss?")
                content=takeCommand()
                to="aadilpar74@gmail.com"
                sendEmail(to , content)
                speak("Email Sent Successfully")
            except Exception as e :
                print(e)
                speak("Sorry Boss an error occured!")    
                
        if'who are you'in query:
            speak("i am Luna created by Aadil Parmar on 13-11-2024 in your service")
        
        if 'play 'in query:
            speak("Playing Random Songs")
            playSong()
            
        
        