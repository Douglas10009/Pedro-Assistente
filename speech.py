import speech_recognition as sr

audio = sr.Recognizer()
# print(sr.Microphone().list_microphone_names())
with sr.Microphone() as source:
    # audio.adjust_for_ambient_noise(source)
    print("Pode falar que eu vou gravar")
    voz = audio.listen(source)
    comando = audio.recognize_google(voz, language="pt-BR")
    print(comando)