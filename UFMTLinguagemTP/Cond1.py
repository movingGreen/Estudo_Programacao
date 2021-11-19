# Classificar uma idade digitada entre: infantil A ou B, Juvenil A ou B, ou Adulto

import sys

def main ():
    idade_pclass = int(input("Digite quantos anos tem o(a) nadador(a): \n"))

    if idade_pclass < 5 : print("Idade muito baixa. ") 

    else :
        if idade_pclass >= 5 and idade_pclass <= 7 :
            print("Esta pessoa está classificada na categoria Infantil A.\n ")
        elif idade_pclass >= 8 and idade_pclass <= 10 :
            print("Esta pessoa está classificada na categoria Infantil B.\n ")
        elif idade_pclass >= 11 and idade_pclass <= 13 :
            print("Esta pessoa está classificada na categoria Juvenil A.\n ")
        elif idade_pclass >= 14 and idade_pclass <= 17 :
            print("Esta pessoa está classificada na categoria Juvenil B.\n ")
        else :
            print("Esta pessoa está classificada na categoria Adulto.\n ")
    
    reiniciar = str(input("Você quer pesquisar outra idade? s/n \n"))
    
    if reiniciar == "s" :
        main()
   
    else :
        sys.exit()

main()