#calcular arcotangente com valor x e número natural p



import sys

#Calculando o valor da arcotangente
def arcoTangente (numX, numP):
    if not numX <= 1 and numX >= 0 : reset()
    if numP < 0 : reset()
    print('tudo certo')
    
    k = 3
    contArcoTan = numX
    cont = 1

    while True :
        
        if (cont % 2) == 0 :

            contArcoTan += (numX ** k) / k

        else: 

            contArcoTan -= (numX ** k) / k
        
        cont += 1
        k += 2
        limiteCont = (numX ** k) / k

        if not abs(limiteCont) < (10 ** (- numP)): break

    print('Arco tangente de', numX, 'é :', contArcoTan)    

#pegando o número real e o número inteiro
def pegarDados():
    
    try :
        realX = float(input("Digite um número real entre 0 e 1: "))
    except:
        sys.exit('==========Entrada não aceita=========')

    try :
        numP = int(input("Digite um número inteiro positivo para as casas de precisão: "))
    except:
        sys.exit('==========Entrada não aceita=========')
    
    return realX, numP

def main():
    x = pegarDados()
    arcoTangente(x[0], x[1]) 

    reset()

#Reiniciando o código
def reset():

    reset = input('Quer contar de novo? (s/n)\n')
    reset = reset.lower()
        
    if reset == 's':
        main()
    else:
        sys.exit()    


main()
