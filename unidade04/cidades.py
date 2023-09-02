
def ler_cidades():
    cidades =[]
    for linha in open("cidades.txt","r"):
        cidades.append(linha.strip().upper())
    return cidades 
   