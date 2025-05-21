import pyttsx3
import schedule
import time
import speech_recognition as sr
from datetime import datetime

# ✅ Initialize text-to-speech engine once for better performance
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Speech speed
engine.setProperty('volume', 1.0)  # Volume level

def speak(text):
    """AI voice reminder bolega"""
    print(f"[Reminder] {text}")  # Console me bhi print karega
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
                print("Reminder stopped.")
                return True
        except Exception as e:
            print(f"Error in voice recognition: {e}")
    return False

def reminder(message):
    """Reminder ko tab tak repeat karo jab tak user 'OK' na bole"""
    try:
        while True:
            speak(message)
            if listen_for_ok():
                break
            time.sleep(5)  # 5 sec baad dubara bolega
    except Exception as e:
        print(f"Error in reminder: {e}")

# ✅ **Fixed Time Reminders**
schedule.every().day.at("07:00").do(reminder, "Good Morning! Have a great day ahead.")
schedule.every().day.at("09:00").do(reminder, "Take your medicine.")
schedule.every().day.at("09:30").do(reminder, "It's time for breakfast.")
schedule.every().day.at("12:00").do(reminder, "Good Afternoon! Keep up the good work.")
schedule.every().day.at("13:30").do(reminder, "It's lunchtime! Eat well.")
schedule.every().day.at("18:00").do(reminder, "Back to work! Stay focused.")
schedule.every().day.at("21:00").do(reminder, "It's dinner time! Enjoy your meal.")
schedule.every().day.at("22:00").do(reminder, "Good Night! Sleep well.")
schedule.every().day.at("23:00").do(reminder, "Good Night! Sweet dreams.")

# ✅ **Interval-Based Reminders (Only Between 7 AM - 10 PM)**
def check_and_remind(message):
    """Ye function sirf 7 AM - 10 PM ke beech interval reminders dega"""
    current_time = datetime.now().time()
    start_time = datetime.strptime("07:00", "%H:%M").time()
    end_time = datetime.strptime("22:00", "%H:%M").time()

    if start_time <= current_time <= end_time:
        print(f"[INFO] Running reminder: {message}")
        reminder(message)

# Drink Water Reminder (Every 30 Min)
schedule.every(30).minutes.do(check_and_remind, "Drink Water! Stay Hydrated.")

# Walk Reminder (Every 3 Hours)
schedule.every(3).hours.do(check_and_remind, "Time to walk! Stay active.")

# Social Media Break Reminder (Every 1 Hour)
schedule.every(1).hours.do(check_and_remind, "Back to work! Avoid distractions.")

# ✅ **Loop to keep script running**
print("[INFO] Reminder script is running...")
while True:
    schedule.run_pending()
    time.sleep(30)  # Check every 30 seconds
