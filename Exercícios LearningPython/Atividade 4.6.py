import sys
def computePay (horasT, pagH):
    try :
        horasT = float(horasT)
        pagH = float(pagH)
    except :
        sys.exit('Digite somente números...')
    horasEx = 0
    pagEx = 0
    if horasT > 40 :
        horasEx = horasT - 40
        pagEx = horasEx * (pagH * 1.5)
    return (((horasT - horasEx) * pagH) + pagEx)

horasTrab = input('Digite a quantidade de horas trabalhadas: ')
pagHora = input('Digite o valor do pagamento por hora: R$')
print('O valor total é: R$'+ str(computePay(horasTrab, pagHora)))