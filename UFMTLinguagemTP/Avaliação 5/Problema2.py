#Programa que le a quantidade de alunos, nomes, idades, generos
#Depois deve mostrar a pessoa mais alta, a mais velha e a porcentagen de mulheres

import sys

#calculador da maior altura
def calcAltu(nomesList, alturaList, genList):
    
    maiorAlt = max(alturaList)
    
    aux1 = alturaList.index(maiorAlt)

    return nomesList[aux1], maiorAlt, genList[aux1]

#calcular a maior idade
def calcIdade(nomesList, idadeList, genList):
    
    maiorIdade = min(idadeList)
    
    aux1 = idadeList.index(maiorIdade)

    return nomesList[aux1], maiorIdade, genList[aux1]

#calcular porcentagem de mulheres
def calcMulheres(quantAl, quantMulh):
    
    porcent = (quantMulh / quantAl) * 100

    return porcent


#inicia os nomes, idades, alturas e genero
#Masculino
nomesM = list()
alturaM = list()
idadeM = list()
generoM = list()

#Feminino
nomesF = list()
alturaF = list()
idadeF = list()
generoF = list()

try:
    quantAlunos = int(input('Digite a quantidade de alunos na sala: '))
except:
    sys.exit('Valor não aceito...........')

for i in range(quantAlunos):

    x1 = input('Digite o nome do(a) aluno(a): ')

    try:
        x2 = int(input('Digite a idade do(a) aluno(a): '))
    except:
        sys.exit('Valor não aceito...')
    
    try:
        x3 = float(input('Digite a altura do(a) aluno(a): '))
    except:
        sys.exit('Valor não aceito...')

    x = input('Digite o gênero do(a) aluno(a): (H/M)\n')
    
    x = x.upper()
    
    if x == 'H':
       
        nomesM.append(x1)
        idadeM.append(x2)
        alturaM.append(x3)
        generoM.append(x)

    elif x == 'M':
        
        nomesF.append(x1)
        idadeF.append(x2)
        alturaF.append(x3)
        generoF.append(x)

    else :
        sys.exit('Valor não aceito...')

a, b, c = calcAltu(nomesM, alturaM, generoM)

print("Homem mais alto: " + str(a) + '\t| ' + str(b) + '\t| ' +str(c))

a, b, c = calcAltu(nomesF, alturaF, generoF)

print("Mulher mais alta: " + str(a) + '\t| ' + str(b) + '\t| ' +str(c))

a, b, c = calcIdade(nomesM, idadeM, generoM)

a1, b1, c1 = calcIdade(nomesF, idadeF, generoF)

print("Homem mais jovem: " + str(a) + '\t| ' + str(b) + '\t| ' +str(c) + '\nMulher mais jovem: ' + str(a1) + '\t| ' + str(b1) + '\t| ' +str(c1))

print("A diferença entre o homem e a mulher mais jovem é: " + str(abs(b-b1)))

porcentF = calcMulheres(quantAlunos, len(nomesF))

print("Quantidade de mulheres na sala: " + str(len(nomesF)) + '\t| ' + str(porcentF) + '%')
