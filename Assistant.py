import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import datetime

r = sr.Recognizer()
phone_numbers = {"sudarshan" : '9876543210', "rahul" : '1234567890', "rohan" : '9876543219'}
account_numbers = {"sbi": '00981238', "hdfc": '00981239', "icici": '00981240'}

def speak(command):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(command)
    engine.runAndWait()

def commands():
    try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            print("Listening...")
            audioin = r.listen(source)
            
            my_text = r.recognize_google(audioin)
            my_text = my_text.lower()
            print(my_text)

            # Play songs
            if 'play' in my_text:
                my_text = my_text.replace('play', '')
                speak('playing' + my_text)
                pywhatkit.playonyt(my_text)

            # Date
            elif 'date' in my_text:
                speak('Today\'s date is ' + datetime.date.today().strftime("%B %d, %Y"))
            
            # Time
            elif 'time' in my_text:
                speak('The current time is ' + datetime.datetime.now().strftime("%H:%M"))

            # Details about a topic
            elif 'tell about' in my_text: 
                subject = my_text.replace('tell about', '')
                speak(wikipedia.summary(subject, 1))
            
            # Phone numbers
            elif 'phone number' in my_text:
                names = list(phone_numbers)
                for name in names:
                    if name in my_text:
                        speak('phone number of'+name+'is'+ phone_numbers[name])
            
            # Bank account numbers
            elif 'account number' in my_text:
                names = list(account_numbers)
                for name in names:
                    if name in my_text:
                        speak(name+'account number is'+ account_numbers[name])         
            
            else:
                speak("Sorry, I didn't understand that. Please try again.")
    
    except Exception as e:
        speak("I didn't catch that. Please try again.")
        print(e)


speak("Welcome to the project")
while True:
  
  commands()

