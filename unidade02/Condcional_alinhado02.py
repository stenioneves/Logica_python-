# Calcular se o aluno foi aprovado ou não tendo uma nota superior a 5 e frequência superior a 75%

nota=float(input("Digite a nota:"))
frequencia=int(input("Digite sua frequência: "))

if nota >= 5 and frequencia >= 75:
    situacao= "aprovado"
elif nota>=5 or frequencia >= 75:
    situacao=" na recuperação"  
else:
    situacao="reprovado"   

print(f"Você está {situacao}!")