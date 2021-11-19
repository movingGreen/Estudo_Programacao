# comparar a soma dos 2 primeiro digitos e 2 ultimos do número n com a raiz quadrada do número n

import sys
import math

def main() :

    numero_n = int(input("Digite um valor natural de 4 digitos: \n"))
    
    quant_digitos = int(math.floor(math.log10(numero_n))+1)
    if quant_digitos > 4 or quant_digitos < 4 : 
       
        print("Número possui mais ou menos do que 4 digitos")
        
        reiniciar = str(input("Quer testar outro número: (s/n) \n"))
        if reiniciar == "s" :
            main()
        else : 
            sys.exit()


    doisp_digit = numero_n // 100
    print ("Os dois primeiros digitos são: ", doisp_digit)

    doisu_digit = numero_n - (doisp_digit * 100)
    print ("Os dois ultimos digitos são: ", doisu_digit)


    if (doisu_digit + doisp_digit) == math.sqrt(numero_n) :
        print("SIM, raiz quadrada igual a soma das duas dezenas")

    else :
        print("NÃO, raiz quadrada não é igual a soma das duas dezenas")

    reiniciar = str(input("Quer testar outro número: (s/n) \n"))

    if reiniciar == "s" :
        main()
    else : 
        sys.exit()

main()