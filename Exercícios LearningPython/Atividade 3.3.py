import sys
try :
    nota = float(input('Digite a pontuação de 0 a 1.0 : '))
except:
    sys.exit('Não é um valor numérico...')
if nota > 1.0 or nota < 0 :
    print('Pontuação fora da escala...')
else :
    if nota >= 0.9 :
        print('Pontuação =', nota, '\nGrade : A')
    elif nota >= 0.8 :
        print('Pontuação =', nota, '\nGrade : B')
    elif nota >= 0.7 :
        print('Pontuação =', nota, '\nGrade : C')
    elif nota >= 0.6 :
        print('Pontuação =', nota, '\nGrade : D')
    else:
        print('Pontuação =', nota, '\nGrade : F')