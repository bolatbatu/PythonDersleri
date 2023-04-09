import openai
import speech_recognition as sr
import pyttsx3

# OpenAI API anahtarınızı buraya girin
openai.api_key = "YOUR_API_KEY"

# Text-to-speech engine initialization
engine = pyttsx3.init()

# Define a function to speak the text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Define a function to recognize the speech
def recognize_speech():
    # Initialize recognizer
    r = sr.Recognizer()

    # Use the default microphone as the audio source
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        # Convert audio to text using Google Speech Recognition
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-US')
        print(f"You said: {query}\n")

    except sr.UnknownValueError:
        # Handle unrecognized speech
        print("I could not understand what you said.")
        query = None

    return query

# Define a function to execute the command
def execute_command(command):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=command,
        max_tokens=100
    )

    speak(response.choices[0].text)

# Loop to continuously listen for commands
while True:
    speak("What would you like me to do?")
    command = recognize_speech()

    if command is not None:
        execute_command(command.lower())
