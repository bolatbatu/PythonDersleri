import speech_recognition as sr
import torch
import openai
import whisper

# Dil modeli yükleme
model_path = "dil_modeli.pt"
model = torch.load(model_path)

# OpenAI ChatGPT API anahtarını ayarlama
openai.api_key = "your_api_key_here"

# Ses tanıma için mikrofonu ayarlama
r = sr.Recognizer()
mic = sr.Microphone()

# Arka plan gürültüsünü ölç ve filtrele
with mic as source:
    r.adjust_for_ambient_noise(source)

print("Chat başlatıldı.")

while True:
    # Kullanıcının konuşmasını dinleme
    with mic as source:
        audio = r.listen(source)

    # Konuşmayı metne dönüştürme
    try:
        text = r.recognize_google(audio, language='tr-tr')
        print("Konuştuğunuz metin: " + text)
    except sr.UnknownValueError:
        print("Ne dediğinizi anlayamadım.")
        continue
    except sr.RequestError as e:
        print("Ses tanıma servisine erişilemedi; {0}".format(e))
        continue

    # ChatGPT modelini kullanarak cevap oluşturma
    prompt = "User: {}\nChatbot:".format(text)
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        temperature=0.7,
        max_tokens=100,
        n=1,
        stop=None,
        timeout=15,
    )

    # Cevabı alma ve ekrana yazdırma
    message = response.choices[0].text.strip()
    print("Chatbot: " + message)

    # Sesli yanıt oluşturma
    whisper.say(message)
