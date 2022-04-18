from gtts import gTTS
from playsound import playsound

audio = 'audio.mp3'
print('O texto precisa ser digitado na lingua escolhida.')
OpcaoLingua = input(
    'Escolha uma opção de lingua, digite 0 para ouvir um texto em Português ou 1 para ouvir um texto em Inglês: ')
escrita = ''
language = ''


if(OpcaoLingua == '0'):
    language = 'pt-br'
    escrita = input('Digite alguma coisa: ')

elif(OpcaoLingua == '1'):
    language = 'en-us'
    escrita = input('Type something: ')

else:
    print('Não entendi a opção escolhida.')


sp = gTTS(
    text=escrita,
    lang=language
)

sp.save(audio)
playsound(audio)
