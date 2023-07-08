#Leia dois valores (inteiros, reais ou caracteres) para as variáveis A e B,
# e efetue a troca dos valores de forma que a variável A passe a possuir o valor da variável B 
#e a variável B passe a possuir o valor da variável A. Apresente os valores trocados.

a=input("Digite o valor de A:")
b=input("Digite o valor de B:")
aux=a
print(f"Valor informado A:{a} e B:{b}")
a=b
b=aux
print(f"Valores trocados A:{a} e B:{b}")
