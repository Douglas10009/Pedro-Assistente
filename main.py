import os
import speech_recognition as sr
import pyttsx3
import datetime
import pygame
import wikipedia
import pywhatkit

'''
Para instalar o PyAudio para o python3.6+ baixe o arquivo :

baixa o arquivo PyAudio-0.2.11-cp39-cp39-win_amd64 (cp39 equivale ao Python 3.9 e AMD64 é para windows com arquitetura 64x) neste link: https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio
No diretório que o arquivo foi baixado execute o comando via terminal: pip install (Local onde você baixou o arquivo)
'''


audio = sr.Recognizer()
maquina = pyttsx3.init()
pygame.init()

start = pygame.mixer.Sound("sounds\start.mp3")
loading = pygame.mixer.Sound("sounds\loading.mp3")
end = pygame.mixer.Sound("sounds\end.mp3")


def executa_comando():
    try:
        with sr.Microphone() as source:
            audio.adjust_for_ambient_noise(source)

            print('Ouvindo...')

            # Recurso sonoro para avisar que o assistente está te escutando
            start.play()

            voz = audio.listen(source)
            # Recurso sonoro para avisar que o assistente parou de escutar
            end.play()

            comando = audio.recognize_google(voz, language='pt-BR')
            comando = comando.lower()
            pygame.quit()

            print('\n' + comando + '\n')

            # Retira o nome do assistente para não dar erro no código
            if 'pedro' in comando:
                comando = comando.replace('pedro', '')
                print(comando)

    except:
        print('Microfone não está ok...')

    try:
        return comando
    except:
        return " "


def comando_voz_usuario():
    comando = executa_comando()

    if any(x in comando for x in ['o que você pode fazer?', 'o que voce pode faze']):
        maquina.say(
            "Bem, eu posso: Dizer as horas, procurar por algo na internet, tocar alguma música no youtube.")
        maquina.runAndWait()

    elif 'horas' in comando:
        hora = datetime.datetime.now().strftime('%H:%M')
        maquina.say('Agora são ' + hora)
        maquina.runAndWait()

    elif any(x in comando for x in ["procure por", "o que é"]):
        procurar = comando.replace('procure por', '')

        maquina.say('Procurando por' + procurar)
        maquina.runAndWait()

        try:
            wikipedia.set_lang('pt')
            resultado = wikipedia.summary(procurar, 2)
            print(resultado)
            maquina.say(resultado)
            maquina.runAndWait()
        except:
            maquina.say('Não encontrei nada sobre...')
            maquina.runAndWait()

    elif 'toque' in comando:
        try:
            musica = comando.replace('toque', '')
            resultado = pywhatkit.playonyt(musica)
            print(resultado)

            maquina.say('Tocando ' + musica)
            maquina.runAndWait()
        except:
            maquina.say('Sinto muito, não encontrei essa música')
            maquina.runAndWait()

    elif 'navegador' in comando:
        maquina.say('Abrindo o Chrome')
        maquina.runAndWait()

        try:
            os.system('start chrome.exe')
        except:
            falar('Não encontrei o Chrome...')
    
    elif 'quanto é' in comando:
        falar('sinto muito, sou burro e não sei contar ainda, tente mais tarde')
    
    else:
        falar('Não entendi o que você falou...')
        falar('Tente falar')
        falar('Que horas são? ou ')
        falar('Abra o navegador')



def falar(texto):
    maquina.say(texto)
    maquina.runAndWait()


while True:
    comando_voz_usuario()
