#10. Crie um programa que exiba um menu com 5 opções para o usuário. 
#A última opção deve ser "0" para sair do programa. 
#Cada opção do menu deve exibir informações relevantes, sem interação do usuário

print("Selecione as opções:")

print("1- Listar Contatos")
print("2- Excluir Contatos")
print("3- Editar Contatos")
print("4- Novo Contatos")
print("0- sair")
opcao=int(input("Digite o número da opção :"))

if opcao==0:
    print("Você decidiu sair, até logo!")
elif opcao==1:
        print("Listando seus contatos...")
elif opcao==2:
      print("Excluindo seu contato ...")
elif opcao==3:
      print("Editando o contato ...")
elif opcao==4:
      print("Criando novo contato ...")
else:
      print(f"Essa opção '{opcao}'  é inválida!")                         
