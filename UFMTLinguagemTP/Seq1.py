# Calcular a hora, minuto e segundo a partir dos segundos digitados pelo usuário


segundos_total = int(input("Entre a quantidade total de segundos: "))

print ('Essa é a quantidade total de segundos: ', segundos_total)


def horarioCompleto(segundos):

    h = segundos // 3600
    m = segundos % 3600 // 60
    s = segundos % 3600 % 60

    return '{:02d}h:{:02d}m:{:02d}s'.format(h, m, s)

print('Esse é o horário completo: ',  horarioCompleto(segundos_total)) 