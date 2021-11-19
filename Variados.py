

def comTryExcept () :
    print ("testando a impressão de texto")
    testeTry = input('Digite um número: \n')
    try: 
        testeint = int(testeTry)
    except:
        testeint = -1
    if testeint >= 0 :
        print('Bom número')
    else :
        print('mal número')


def matematicas () : 

    import math 

    print(math)
    import random

    for i in range(2) :

        x = random.random()

        print(x)


def loops ():
    while True :
        aux1 = 1
        a = input("'sair' para sair:\n'contar' para contar: \n")
        if a == 'sair' :
            break
        elif a == 'contar' :
            for i in range(5):
                print(aux1)
                aux1 += 1

def palavrasEspec ():
    import keyword
    print(keyword.kwlist)


## for i in ['testando', 123, 'dese', 4 + 10, 'jeito vai qualquer\n======coisa======'] :
##    print(i)


def textCont () :
    palavra = input('Digite a palavra para contar: ')
    modoOperação = input('Digite o modo de contar (a/b/c): ')
    contador = 0
    if modoOperação == 'a' :
        while contador < len(palavra) :
            letra = palavra[contador]
            print('Na posição:', contador, 'Letra:', letra)
            contador += 1
            if contador == len(palavra) : print('Tamanho da palavra:', len(palavra))
    elif modoOperação == 'b' :

        for letras in palavra :
            print(letras)  
            contador += 1
            if contador == len(palavra) : print('Tamanho da palavra:', len(palavra))                   
    elif modoOperação == 'c' :
        print(palavra[3:])
        print(palavra[:2])
        print(palavra[3:5])
        print(palavra[:])
        print(palavra[1:7])

def olharArquivo ():
    arquivo = input('Digite o arquivo para ser olhado: ')
    arqDados = open(arquivo)
    print(arqDados[:30])


def dicionarios():
    dicionario = {}
    dicionario['abc'] = 1
    print('abc' in dicionario)
    if not 'abc' in dicionario :
        print('false')

    contador = {}
    nomes = ['nome1', 'abcdew', 'namão', 'namão', 'mamão', 'nome1', 'namão']
    for palavra in nomes :
        contador[palavra] = contador.get(palavra, 0) + 1
    print(contador)
    print(sorted(contador.items()))

def telnet():
    import socket

    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect(('data.pr4e.org', 80))
    cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
    mysock.send(cmd)

    while True:
        data = mysock.recv(512)
        if len(data) < 1:
            break
        print(data.decode(),end='')
    mysock.close()

    a = 'casa Azul'
    for x in a :
        print(x, ord(x))


    import urllib.request

    fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
    for linha in fhand:
        print(linha.decode().strip())      

    for i in range(10) :
        print(i+1)

x = None
a = 10 
x is None or a > x


def sqliteArchive():
    import sqlite3

    conn = sqlite3.connect('music.sqlite')
    cur = conn.cursor()

    cur.execute('DROP TABLE IF EXISTS Tracks')
    cur.execute('CREATE TABLE Tracks (title TEXT, plays INTEGER)')

    conn.close()


def numpyEstudo():
    import numpy as np
 
    arr = np.array([1,2,3,4,5])

    print(arr)

# numpyEstudo()

def testeSeg():
    x = input("Qual é o seu nome?\n")
    print("Olá {}" .format(x))

testeSeg()