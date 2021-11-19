#%%
from typing import List


testeEspaço = ""

for i in range(3):
    testeEspaço += " "
    print("etapa {} :{}|||" .format(i + 1, testeEspaço))
print("")
print("    1")
print(" 1234")
print("   12")
print("\t9")
print("123456789")
print("\t|")

# %%

lista = "abc"
lista += "-" * 10
lista += "|\n|"
print(lista)
# %%
