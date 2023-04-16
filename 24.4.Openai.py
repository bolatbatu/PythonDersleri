import openai
import speech_recognition as sr
import pyttsx3

openai.api_key = "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"

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def recognize_speech():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Dinliyorum...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Kaydediliyor...")
        query = r.recognize_google(audio, language='tr-TR')
        print(f"Sorunuz: {query}\n")

    except sr.UnknownValueError:
        print("Dediğinizi anlamadım.")
        query = None

    return query

def execute_command(command):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=command,
        max_tokens=100
    )

    speak(response.choices[0].text)

while True:
    speak("Ne yapmamı istersiniz?")
    command = recognize_speech()

    if command is not None:
        execute_command(command.lower())
