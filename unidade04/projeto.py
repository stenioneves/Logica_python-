import os
from colorama import Fore, init
from cidades import ler_cidades
init(autoreset=True) 

def pausar():
    input(f"{Fore.RED}Aperte ENTER para continuar ...")

def limpar_tela():
    os.system('cls'if os.name=="nt" else 'clear')

def processar_opcao(opcao):
    if opcao==1:
        cidades=ler_cidades()
        for cidade in cidades:
            print(f"{Fore.GREEN}-->{cidade}")
    elif opcao==0:
        print(f"{Fore.LIGHTRED_EX}Saindo do sistema")
        return 0
def exibir_menu():
   print(f"{Fore.LIGHTGREEN_EX}=====MENU======")
   print(f"{Fore.CYAN}1. Listar Cidades")
   print(f"{Fore.BLUE}2. Adcionar cidade")
   print(f"{Fore.CYAN}3. Buscar cidade")
   print(f"{Fore.LIGHTWHITE_EX}4. Atualizar cidade")
   print(f"{Fore.YELLOW}5. Excluir cidade")
   print(f"{Fore.RED}0. Sair")

def executar_sistema():
    exibir_menu() 
    opcao=int(input(f"{Fore.YELLOW}Digite a  opção desejada: ")) 
    limpar_tela()
    processar_opcao(opcao) 
    pausar()
    executar_sistema()


executar_sistema()