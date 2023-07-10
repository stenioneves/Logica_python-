#Elabore um programa que efetue a apresentação do valor da conversão em dólar de um valor lido em real. 
#O programa deve solicitar a cotação do dólar e também a quantidade de reais disponível com o usuário, 
#para que seja apresentado o valor em moeda americana.

print("Conversão de real para Dolar Americano")
cotacao_dolar= float(input("Digite a cotação do Dolar :"))
valor_real=float(input("Digite a quantidade de valores em reais(R$):"))
conversao= valor_real/cotacao_dolar
print(f"Cotação do dolar R$ {cotacao_dolar}")
print(f"Valor informado  em R$ {valor_real}")
print(f"Valor convertido : $ {conversao:2f} USD")


