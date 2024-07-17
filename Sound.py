import pyttsx3
def speak_text(text):
    engine=pyttsx3.init()
    rate=engine.getProperty('rate')
    engine.setProperty('rate', rate - 50)
    volume=engine.getProperty('volume')
    engine.setProperty('volume',volume+0.25)
    engine.say(text)
    engine.runAndWait()
speak_text("Hi,how are you?What are you doing?")