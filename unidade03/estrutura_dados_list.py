#Manipulação de list

alunos=["Ana","Pedro"]
print(alunos)
alunos.append("Stenio")
print(alunos)

alunos.remove("Ana")
pesquisa_aluno=input("Digite o nome do Aluno")
if "Stenio" in  alunos:
    print(f"Aluno encontrado ")
else:
    print("Aluno não encontrado")    