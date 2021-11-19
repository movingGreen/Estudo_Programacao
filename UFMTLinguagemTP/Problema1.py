#Receber valores e guardalos em uma matriz 5x5
#E depois compactar eles em uma matriz 3x3 como valor-linha-coluna

linhas = 5
colunas = 5
matrizM = [[0.0 for i in range(colunas)] for j in range(linhas)]

#recebe o input dos valores na matrizM
for i in range(linhas):
    for j in range(colunas):
        print('Digite o valor da posição ['+ str(i) + '] [' + str(j) + '] :')
        matrizM[i][j] = int(input())

#leia a matrizM e guarde os valores-linha-posição compactados na matrizCond
matrizCond = [[0.0, 0.0, 0.0]]
contLinhas = 0
for i in range(linhas):
    for j in range(colunas):
        if matrizM[i][j] > 0 :
            contLinhas += 1
            valorPosi = [matrizM[i][j], i, j]
            if matrizCond[0][0] == 0 :
                matrizCond[0] = valorPosi
                continue
            matrizCond.append(valorPosi)

#print dos valores da matrizCond
print('Valor | Linha | Coluna')
for i in range(contLinhas) :
    print(matrizCond[i])



