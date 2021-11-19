horasT = input('Digite as horas trabalhadas: ')
pagH = input('Digite o pagamento por hora trabalhada: ')
try:
    horasT = float(horasT)
    pagH = float(pagH)
except:
    print('Digite valores numéricos...')
pagE = 0
horasEx = 0
if horasT > 40 :
    horasEx = horasT - 40
    pagE = horasEx * (pagH * 1.5)
print('Pagamento =', (horasT - horasEx) * pagH + pagE)