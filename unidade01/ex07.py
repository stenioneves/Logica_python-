#Efetue o cálculo da quantidade de litros de combustível gasta em uma viagem, 
#utilizando um automóvel que faz 12 Km por litro. Para obter o cálculo, 
#o usuário deve fornecer o tempo gasto (TEMPO) e a velocidade média (VELOCIDADE) durante a viagem. 
#Desta forma, será possível obter a distância percorrida com a fórmula DISTANCIA = TEMPO * VELOCIDADE. 
#Possuindo o valor da distância, basta calcular a quantidade de litros de combustível utilizada 
#na viagem com a fórmula LITROS_USADOS = DISTANCIA / 12. 
# Ao final, o programa deve apresentar os valores da velocidade média (VELOCIDADE), 
#tempo gasto na viagem (TEMPO), a distância percorrida (DISTANCIA)
# e a quantidade de litros (LITROS_USADOS) utilizada na viagem.

tempo=float(input("Digite o tempo em horas :"))
velocidade_media=float(input("Digite a velocidade média em Km/h:"))
distancia= tempo*velocidade_media
litros_usados= distancia/12

print(f"")