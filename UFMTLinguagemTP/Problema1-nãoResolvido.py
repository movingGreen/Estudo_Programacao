# Receber transações financeiras de 1000 contas e informar operações suspeitas, saldos das contas,
# os dois correntistas com maior saldo e o saldo total das operações da agência

import sys

#Criar vetor com as 1000 contas
correnNum = [0.0] * 1000
print(len(correnNum))
     
#Definir as transações de cada conta
operaçãoConta = 1
while operaçãoConta != 0 :
    numeroConta = int(input('Digite o número da conta: \n'))
    operaçãoConta = float(input('Digite o valor da operação: \n'))
    if operaçãoConta > 20000 : print('Operação suspeita movimentou mais do que R$20000')
    correnNum [numeroConta] += operaçãoConta  
    
#Mostrar saldos das contas
maiorCorren1 = 0
maiorCorren2 = 0
for aux1 in correnNum :
    aux2 = 1
    print("Saldo da conta", aux2, "= R$" + str(aux1))
    
#Mostrar dois correntistas com maior saldo
    if aux1 > maiorCorren1 : maiorCorren1 = aux2
    if aux1 > maiorCorren2 : maiorCorren2 = aux2
    aux2 += 1
print('o correntista com maior saldo é o número {:d} com saldo de R${:03f}\n' .format(maiorCorren1,correnNum[maiorCorren1 - 1]))
print('o segundo correntista com maior saldo é o número {:d} com saldo de R${:03f}\n' .format(maiorCorren1,correnNum[maiorCorren2 - 1])) 
agenciaFinal = 0
# Mostar saldo da agência
for aux3 in range(correnNum) :
    agenciaFinal += aux3

print('O saldo total da agência é: R$' + agenciaFinal)