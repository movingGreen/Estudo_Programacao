# receber o número de empregados, valor do salário mínimo, custo de cada bicicleta e número de bicicletas vendidas
# entregar o salário total de cada empregado e o lucro da loja

import sys

n_empregados = int(input("Digite o número de empregados da loja: "))

if n_empregados == 0 :
    sys.exit("O número de empregados é zero então não tem salário para calcular")

valor_smínimo = int(input("Digite o valor do salário mínimo em reais R$: "))
custo_bicicleta = float(input("Digite o custo, para a loja, de cada bicicleta em reais R$: "))
n_bicvendidas = int(input("Digite o número de bicicletas vendidas: "))


valor_venda = float(custo_bicicleta + (0.5 * custo_bicicleta))

valor_comiss = 0

if n_bicvendidas !=0 :
    valor_comiss = ((0.15 * custo_bicicleta) * n_bicvendidas) / n_empregados

lucro_loja = (valor_venda * n_bicvendidas) - ((2 * valor_smínimo) * n_empregados) - (valor_comiss * n_empregados) 

valor_stotal = (2 * valor_smínimo) + valor_comiss

print("O salário total de cada empregado é: R${0:.2f} " .format(valor_stotal))
print("O lucro final da loja é: R${0:.2f}" .format(lucro_loja))

