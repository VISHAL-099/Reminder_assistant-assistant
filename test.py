import pyttsx3
import speech_recognition as sr
import time

def speak(text):
    """AI voice reminder bolega"""
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Speech speed
    engine.setProperty('volume', 1.0)  # Volume level
    engine.say(text)
    engine.runAndWait()

def listen_for_ok():
    """Microphone se suno aur agar user 'OK' bole to reminder stop karo"""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for 'OK'...")
        try:
            audio = recognizer.listen(source, timeout=5)  # 5 sec tak suno
            command = recognizer.recognize_google(audio).lower()
            if "ok" in command:
                print("OK detected! Stopping reminder.")
                return True
        except:
            pass
    return False

def test_reminder():
    """Test Reminder - Jab tak 'OK' nahi bola tab tak repeat hoga"""
    while True:
        speak("Testing reminder. Say OK to stop.")
        if listen_for_ok():
            break
        time.sleep(5)  # 5 sec baad phir se bolega

# 🔥 Testing Function Call
test_reminder()
