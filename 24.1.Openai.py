import openai
import os
from gtts import gTTS
openai.api_key = "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"

a=input("Sorunuzu giriniz. :")
response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=a,
    max_tokens=500
)
print(response)
text= response.choices[0].text.replace("\n","")
print(text)
tts = gTTS(text=text,lang="tr")
tts.save("savefile.mp3")
os.system("savefile.mp3")

