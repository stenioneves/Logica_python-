#Elabore um programa que calcule e apresente o volume de uma caixa retangular, 
#por meio da fórmula VOLUME = COMPRIMENTO * LARGURA * ALTURA.
#Autor: Stenio Neves

print("Calculo de volume  de um objeto retangular")
comprimento=int(input("Digite o comprimento do objeto: "))
largura=int(input("Digite a largura do objeto:"))
altura=int(input("Digite a altura do objeto :"))
#Simplificação
print("O volume é ",comprimento*altura*largura,"M³")
#Continuação do código de forma padrão
volume= comprimento*largura*altura
print(f"O volume é {volume} M³")
