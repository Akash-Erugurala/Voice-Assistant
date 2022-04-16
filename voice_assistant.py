from urllib import request
import pyttsx3 # This model converts text data to speech
import datetime # library for getting date and time
import speech_recognition as sr  # it converts speech from mic to text 
import smtplib  # an inbuilt python library for email
import wikipedia 
import pywhatkit
import requests
from newsapi import NewsApiClient
import clipboard
import pyjokes
import time as tt

from sender import senderemail,epwd,to
from email.message import EmailMessage
import pyautogui
import webbrowser as wb
from time import sleep

engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def getvoices(voice):
    voices = engine.getProperty('voices')
    # print(voices[1].id)
    if voice == 1:
        engine.setProperty('voice',voices[0].id)
        speak("Hello this is Edith")
    
    if voice == 2:
        engine.setProperty('voice',voices[1].id)
        speak("Hello this is vision")
    
    

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S") # hour = I, minutes = M, seconds = S
    speak("The current time is:")
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)
    speak("Today's date is:")
    speak(day)
    speak(month)
    speak(year)


def greeting():
    hour = datetime.datetime.now().hour
    if hour > 6 and hour < 12 :
        speak("Good Morning sir!")
    elif hour >=12 and hour <18:
        speak("Good Afternoon sir!")
    elif hour >=18 and hour < 24:
        speak("Good Evening Sir!")
    else:
        speak("Good Night Sir!")


def wishme():
    speak("Welcome Spoidy!! Edith version loading")
    time()
    date()
    greeting()
    speak("Edith at your service, how can i help you ?")


    
"""while True:
    voice = int(input("Press 1 for male voice\nPress 2 for female voice\n"))

  #  speak(audio)
    getvoices(voice) 
"""
#wishme()

def takeCommandCMD():
    query = input("Please tell me how can i help you ?\n")
    return query 


def takeCommandMic():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language="en-IN")
        print(query)
    except Exception as e:
        print(e)
        speak("Sorry, please say that again...")
        return "None"
    return query

def sendEmail(receiver, subject,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(senderemail,epwd)
    email = EmailMessage()
    email['From'] = senderemail
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(content)
    server.send_message(email)
    server.close()
    
def sendwhatsmsg(phone_no,message):
    Message = message
    wb.open('https://web.whatsapp.com/'+phone_no+'&text='+Message)
    sleep(10)
    pyautogui.press('enter')

def searchgoogle():
    speak('What should i search for?')
    search = takeCommandMic()
    wb.open('https://www.google.com/webhp?hl=en&ictx=2&sa=X&ved=0ahUKEwjr4L_G0p_zAhW_zDgGHf--DfIQPQgJ'+search)

def news():
    newsapi = NewsApiClient(api_key='f0eaad4ddbdd484ab5259dff3dbbd46f')
    speak('What topic you need the news about?')
    topic = takeCommandMic()
    data = newsapi.get_top_headlines(q=topic,
                                    language ='en',
                                    page_size = 5)
    newsdata = data['articles']
    for x,y in enumerate(newsdata):
        print(f'{x}{y["description"]}')
        speak( print(f'{x}{y["description"]}'))
    speak("that's it for now i'll upate you in some time")

def text2speech():
    text = clipboard.paste()
    print(text)
    speak(text)

def covid():
    r = requests.get('https://coronavirus-19-api.herokuapp.com/all')
    data = r.json()
    covid_data = f'Confirmed cases : {data["cases"]} \n Deaths :{data["deaths"]} \n Recovered :{data["recovered"]}'
    print(covid_data)
    speak(covid_data)

def screenshot():
    name_img = tt.time()
    name_img = f'D:\SS_Voice\\{name_img}.png'
    img = pyautogui.screenshot(name_img)
    img.show()






if __name__ == "__main__":
    getvoices(2)

    wishme()
    while True:
       # query = takeCommandCMD().lower()
        query = takeCommandMic().lower()

        if 'time' in query:
            time()

        elif 'date' in query:
            date()
        elif 'email' in query:
            email_list = {
                'ghost': 'vishnupriyabts2020@gmail.com',
                'friend':'akasherugurala5@gmail.com',
                'Ankit':'ankitbhagatrock392000@gmail.com',
                'roommate':'dilipsinghbaghel81@gmail.com'
            }
            try:
                speak("To whom you want to send the mail?")
                name = takeCommandMic()
                receiver = email_list[name]
                speak("What is the subject of the mail")
                subject = takeCommandMic()
                speak('What should i say ?') 
                content = takeCommandMic()
                sendEmail(receiver, subject , content)
                speak("Email has been sent successfully.")
            except Exception as e:
                print(e)
                speak("Unable to send the email, please try again")

        elif 'message' in query:
            user_name = {
                'friend':'+91 85008 26897',
                'brother':'+91 70707 15329'}
            try:
                speak("To whom you want to send the message?")
                name = takeCommandMic()
                phone_no = user_name[name]
                speak("What is the message to be sent")
                message = takeCommandMic()
                sendwhatsmsg(phone_no,message)
                speak("Message has been sent successfully.")
            except Exception as e:
                print(e)
                speak("Unable to send the message, please try again")  
        
        elif 'wikipedia' in query:
            speak('searching on wikipedia..')
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query,sentences = 2)
            print(result)
            speak(result)

        elif 'search' in query:
            searchgoogle()

        elif 'youtube' in query:
            speak('What should i search for on youtube?')
            topic = takeCommandMic()
            pywhatkit.playonyt(topic)
        
        elif 'weather' in query:
            url = 'http://api.openweathermap.org/data/2.5/weather?q=Delhi&units=imperial&appid=1e8b90b3d28c23644c48c26b59695d2d'
            
            res = requests.get(url)
            data = res.json()

            weather = data['weather'] [0] ['main']
            temp = data['main']['temp']
            description = data['weather'][0] ['description']
            temp = round((temp - 32)*5/9)
            print(weather)
            print(temp)
            print(description)
            speak('Temperature :{} degree celcius'.format(temp))
            speak('Weather is {}'.format(description))
        
        elif 'news' in query:
            news()
        
        elif 'read' in query:
            text2speech()
        
        elif 'covid' in query:
            covid()
        
        elif 'joke' in query:
            speak(pyjokes.get_joke())
        
        elif 'screenshot' in query:
            screenshot()



        elif 'offline' in query:
            quit()

    

 
