cont = 0
total = 0
while True :
    numero = input('Digite um número: ')
    if numero == 'pronto' :
        break
    try:
        numero = float(numero)
    except:
        print('Digite somente números...')
        continue
    total += numero
    cont += 1 
if cont == 0 :
    print('O total é:', total, 'A quantidade é:', cont, 'A média é:', 0)
else: 
    print('O total é:', total, 'A quantidade é:', cont, 'A média é:', total/cont)