
import random
import operacoes
from colorama import Fore, init
init(autoreset=True)

def exibir_menu():
    print(f"{Fore.GREEN}1. Soma")
    print(f"{Fore.BLUE}2. Subtração")
    print(f"{Fore.MAGENTA}3. Mutiplicação")
    print(f"{Fore.YELLOW}4. Divisão")
    print(f"{Fore.LIGHTBLACK_EX}5. Numero aletório")
    print(f"{Fore.LIGHTRED_EX}0. Sair")
   

def obter_numeros():
    a= float(input("Digite o primeiro número: "))
    b= float(input("Digite o segundo número: "))
    return [a,b]
   
while True:
        exibir_menu()
        opcao= int(input("Selecione uma opção: "))

        if(opcao==0):
            print("Saindo ...")
            break      
        elif(opcao==1):
            a,b=obter_numeros()
            print(f"Resultado: {operacoes.soma(a,b)}")    
        elif(opcao==2):
            a,b=obter_numeros()
            print(f"Resultado: {operacoes.subtracao(a,b)}")
        elif(opcao==3):
            a,b=obter_numeros()
            print(f"Resultado: {operacoes.mutiplicacao(a,b)}") 
        elif(opcao==4):
            a,b=obter_numeros()
            if(b!=0):
                print(f"Resultado {operacoes.divisao(a,b)}")
            else:
                print("Não é possível dividir por zero! ")    
        elif(opcao==5):
            a,b=obter_numeros()
            print(f"Numero gerado : {random.randint(a,b)}")
        else:
            print(f"{Fore.RED}Opção inválida !!")                