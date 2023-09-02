from colorama import Fore, init
init(autoreset=True)
def ler_arquivo(nome_arquivo):

    arquivo=open(nome_arquivo,"r")
    conteudo= arquivo.read()
    arquivo.close()
    print(f"{Fore.YELLOW}Lendo o arquivo :{nome_arquivo}")
    print(conteudo)
    #return conteudo


def escrever_arquivo(nome_arquivo,conteudo):
    arquivo=open(nome_arquivo,"w")
    arquivo.write(conteudo)
    arquivo.close()

def adicionar_arquivo(nome_arquivo,conteudo):
    arquivo=open(nome_arquivo,"a")
    arquivo.write(conteudo)
    arquivo.close()

def ler_linha_arquivo(nome_arquivo):
    print(f"{Fore.BLUE}Lendo o arquivo :{nome_arquivo}")
    for linha in open(nome_arquivo,"r"):
        print(f"==> {linha.strip()}")

ler_arquivo("cidades.txt")
escrever_arquivo("cidades.txt","Riberão Preto\n")
ler_arquivo("cidades.txt")
adicionar_arquivo("cidades.txt","Sorocaba\n")
ler_arquivo("cidades.txt")
ler_linha_arquivo("cidades.txt")