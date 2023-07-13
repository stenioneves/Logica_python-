#Estrutura de repetição FOR
# Programa simples de Tabuada
#Exercicio em aula.

numero= int(input("Digite o numero :"))
print(f"Tabuada do número : {numero}")
for i in range(1,11): # range traz uma seguencia de números.
    resultado= numero*i
    print(f"{numero} X {i} = {resultado}")