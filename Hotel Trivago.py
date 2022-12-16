import random
import os
menuB = 1
menuA = 0
days = 0
discount = 0
roomservice = []
turism = []
for count in range (100):

    print("                       .|")
    print("                       | |")
    print("                       |'|            ._____")
    print("               ___    |  |            |.   |' .---|")
    print("       _    .-'   '-. |  |     .--'|  ||   | _|    |")
    print("    .-'|  _.|  |    ||   '-__  |   |  |    ||      |")
    print("    |' | |.    |    ||       | |   |  |    ||      |")
    print(" ___|  '-'     '    ""       '-'   '-.'    '`        |____")

    print("                _           _       _ ")
    print("               | |         | |     | |")
    print("               | |__   ___ | |_ ___| |")
    print("               | '_ \ / _ \| __/ _ \ |")
    print("               | | | | (_) | ||  __/ |")
    print("               |_| |_|\___/ \__\___|_|")
    os.system('cls')

name = input("Bem Vindo ao Hotel, é um prazer ter você aqui no nosso sistema de reservas automatico!\nPara começarmos, digite seu nome!")

while menuB == 1:
    person = int(input("Deseja Reservar para quantas pessoas ? \n"))
    if person > 15:
        print("Numero de pessoas ultrapassa o limite de hospedes!! >:(")
        menuB = 1
    else:
        menuB = 0

days = int (input("Quantos dias deseja permanecer no Hotel? \n"))
if days >= 10 and days < 20:
    discount = 0.05
elif days >= 20:
    discount = 0.1
while menuA == 0:
 menuA =  int(input("Qual tipo de quarto vai ficar ? \n 1-- Solteiro \n 2-- Casal \n 3-- Solteiro Duplo \n 4-- Suite Master \n 5-- Cobertura \n "))
 match menuA:
    case 1:
        if person > 1:
            print("Quarto não recomendado para esse numero de pessoas!")
            menuA = 0
        else:
             valor = 200
             roomservice = {'Café': [100], 'Almoço': [200], 'Tudo Incluso': [350], 'Nenhum': [0]}
             option = input ("Qual serviço você deseja ?")
             optionA = input ("Deseja translado durante sua estadia?")
             turism = {'Sim': [200], 'Não': [0]}
             valor = days * (person * (valor + roomservice[option][0] + turism[optionA][0]))
             discount = valor * discount
             valor = valor - discount
             print(valor)
             
    case 2: 
        if person > 2: 
            print ("Quarto não recomendado para esse numero de pessoas!")
            menuA = 0
        else:
             valor = 250
             roomservice = {'Café': [100], 'Almoço': [200], 'Tudo Incluso': [350], 'Nenhum': [0]}
             option = input ("Qual serviço você deseja ?")
             optionA = input ("Deseja translado durante sua estadia?")
             turism = {'Sim': [200], 'Não': [0]}
             valor = person * (valor + roomservice[option][0] + turism[optionA][0])
             discount = valor * discount
             valor = valor - discount
             print(valor)
    case 3:
        if person > 2: 
            print ("Quarto não recomendado para esse numero de pessoas!")
            menuA = 0
        else:
             valor = 250
             roomservice = {'Café': [100], 'Almoço': [200], 'Tudo Incluso': [350], 'Nenhum': [0]}
             option = input ("Qual serviço você deseja ?")
             optionA = input ("Deseja translado durante sua estadia?")
             turism = {'Sim': [200], 'Não': [0]}
             valor = person * (valor + roomservice[option][0] + turism[optionA][0])
             discount = valor * discount
             valor = valor - discount
             print(valor)
    case 4:
        if person > 3: 
            print ("Quarto não recomendado para esse numero de pessoas!")
            menuA = 0
        else:
             valor = 700
             roomservice = {'Café': [100], 'Almoço': [200], 'Tudo Incluso': [350], 'Nenhum': [0]}
             option = input ("Qual serviço você deseja ?")
             optionA = input ("Deseja translado durante sua estadia?")
             turism = {'Sim': [200], 'Não': [0]}
             valor = person * (valor + roomservice[option][0] + turism[optionA][0])
             discount = valor * discount
             valor = valor - discount
             print(valor)
    case 5:
        if person > 15: 
            print ("Quarto não recomendado para esse numero de pessoas!")
            menuA = 0
        else:
             valor = 1500
             roomservice = {'Café': [100], 'Almoço': [200], 'Tudo Incluso': [350], 'Nenhum': [0]}
             option = input ("Qual serviço você deseja ?")
             optionA = input ("Deseja translado durante sua estadia?")
             turism = {'Sim': [200], 'Não': [0]}
             valor = person * (valor + roomservice[option][0] + turism[optionA][0])
             discount = valor * discount
             valor = valor - discount
             print(valor)


