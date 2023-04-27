import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Lütfen konuşun...")
    audio = r.listen(source)

try:
    text = r.recognize_google(audio, language='tr-tr')
    print("Konuştuğunuz metin: " + text)
except sr.UnknownValueError:
    print("Ne dediğinizi anlayamadım.")
except sr.RequestError as e:
    print("Ses tanıma servisine erişilemedi; {0}".format(e))