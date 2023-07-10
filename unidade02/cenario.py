#Cálculo de salário de um pessoa PJ, exercicio proposto em aula.
# Bônus com de R$ 500 acima de 100h
#Bloco de  controle


total_horas=float(input("Digite a quantidade de horas trabalhadas: "))
valor_horas=float(input("Digite o valor da hora de trabalho R$:"))

if(total_horas>= 100):
    bonus= 500.0
else:
    bonus =0.0    
salario=total_horas*valor_horas+bonus
print(f"Seu salário é R$ : {salario}")