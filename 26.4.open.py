import speech_recognition as sr
import torch
import openai
import pyttsx3

# OpenAI ChatGPT API anahtarını ayarlama
openai.api_key =  "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"

# Ses tanıma için mikrofonu ayarlama
r = sr.Recognizer()
mic = sr.Microphone()

## Arka plan gürültüsünü ölç ve filtrele
#with mic as source:
#    r.adjust_for_ambient_noise(source)

# TTS motoru oluşturma
engine = pyttsx3.init()

# Kullanıcının konuşmasını dinleme ve metne dönüştürme
while True:
    with mic as source:
        print("Sizi dinliyorum...")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio, language='en-en')
        print("Söylediğiniz metin: " + text)

        # ChatGPT modeli ile cevap üretme
        prompt = "Kullanıcı: " + text + "\nChatbot:"
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )

        message = response.choices[0].text.strip()
        print("Chatbot: " + message)

        # Yanıtın sesli hale getirilmesi ve oynatılması
        engine.say(message)
        engine.runAndWait()

    except sr.UnknownValueError:
        print("Ne dediğinizi anlayamadım.")
    except sr.RequestError as e:
        print("Ses tanıma servisine erişilemedi; {0}".format(e))
