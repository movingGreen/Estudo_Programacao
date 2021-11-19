#Receber o gabarito das 20 questões, os nomes dos 30 candidatos e as 20 respostas dos 30 candidatos
#Mostrar a porcentagem de candidatos em cada pontuação, a porcentagem de acertos em cada questão
#o nome e a pontuação de cada candidato e o nome do candidato com a melhor pontuação
#Questões da 16 à 20 valem mais para a classificação

quantQuest = 6
quantCand = 4
gabarito = [''] * quantQuest

#receba o gabarito
for i in range(quantQuest):
    print('Digite o gabarito da questão', i + 1, ': ')
    gabarito[i] = str(input())

#receba os nomes e respostas de cada candidato
candidatosNomes = [''] * quantCand
candidatosResp = [[''] * quantQuest]
respAux = [''] * quantQuest

for i in range(quantCand):
    print('Digite o nome do candidato:')
    candidatosNomes[i] = str(input())

    for j in range(quantQuest):
        print('Digite a resposta da questão', j + 1, ':')
        respAux[j] = str(input())

    if i == 0 : 
            candidatosResp[i] = respAux
            continue

    candidatosResp.append(respAux)

#pontuação de cada candidato e a melhor pontuação em geral
candidatosNotas = [0] * quantCand
questMaisV = [0] * quantCand
for i in range(quantCand):

    for j in range(quantQuest):

        if candidatosResp[i][j] == gabarito[j] :
            candidatosNotas[i] += 1
            if j == 5 or j == 6  :
                questMaisV[i] += 1
print (candidatosNotas)

maiorNota = None
candComMNota = 0
print('=======================')
for i in range(quantCand):
    print('Candidato', i + 1, 'acertou', candidatosNotas[i], 'questões' ) 
print('=======================')

for i in range(quantCand):

    if maiorNota is None: 
        
        maiorNota = candidatosNotas[i]
        candComMNota = i

    elif candidatosNotas[i] >= maiorNota and questMaisV[i] > questMaisV[i - 1]: 
        
        maiorNota = candidatosNotas[i]
        candComMNota = i

print('=======================')
print('O candidato com a melhor nota é o nº:' + str(candComMNota) + ' de nota', maiorNota)
print('=======================')

#mostrar a porcentagem de candidatos em cada pontuação


#a porcentagem de acertos em cada questão


