#Elabore um programa que efetue a leitura de três valores (A, B e C) 
#e apresente como resultado final a soma dos quadrados dos três valores lidos..


a=int(input("Digite o valor de A: "))
b=int(input("Digite o valor de B: "))
c=int(input("Digite o valor de C: "))

#a=(a*a)
q_a=(a*a)
q_b=(b*b)
q_c=(c*c)
soma=q_a+q_b+q_c
print("Valores informados ")
print(f"A:{a} seu quadrado é: {q_a}")
print(f"B:{b} seu quadrado é: {q_b}")
print(f"A:{c} seu quadrado é: {q_c}")
print(f"A soma dos quadrados de A {q_a}, B: {q_b} e C: {q_c} é :{soma}")
