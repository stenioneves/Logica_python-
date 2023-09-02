#Manipulação de list

alunos=["Ana","Pedro"]
print(alunos)
alunos.append("Stenio")
print(alunos)

alunos.remove("Ana")
pesquisa_aluno=input("Digite o nome do Aluno: ")
if pesquisa_aluno in  alunos:
    print(f"Aluno {pesquisa_aluno} encontrado ")
else:
    print("Aluno não encontrado")    
