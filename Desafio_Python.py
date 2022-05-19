from random import choice
from time import sleep
opcoes = ['afobado','amendoim','banheiro','caatinga','cachorro','campeonato','capricornio','catapora','corrupçao','crepusculo','empenhado',
'esparadrapo','forca','galaxia','historia','magenta','manjericao','menta','moeda','oraçao','paçoca','palavra',
'pedreiro','pneumonia','pulmao','rotatoria','serenata','transeunte','trilogia','xicara']
palavra = choice(opcoes)
lista = list(palavra)
nome = input('Qual é o seu nome? ')
print(f"""Bem vindo ao jogo', {nome} '!'
Tente descobrir a palavra! Tente letra por letra!

Mas não erre mais que 5 letras!!

Vou pensar em uma palavra .... """)
sleep(2)
print('A palavra tem',len(lista) , 'letras.')
acertos = []
erros = certo = 0
for l in range(0, len(lista)):
    acertos.append('_')
while True:
    conta = 0
    letra = input('Informe uma letra: ')
    while letra.isalpha() != True:
        print('Digite somente letras! Números não são permitidos.')
        letra = input('Informe uma letra: ')
    for i in range(0, len(lista)):
        if letra == lista[i]:
            acertos[i]=letra
            certo += 1
        else:
            conta += 1
    if certo == len(lista):
        print('Parabéns!!! Descobriu a palavra.')
        break
    if conta == len(lista):
        erros += 1
        print('Erros:', erros)
    if erros > 5:
        print('Você perdeu! A palavra era', palavra)
        break
    print(acertos) 
               