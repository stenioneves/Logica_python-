#Programa que classifique o desenvolvedor conforme o tempo de experiência.
#Exercício de aula


anos_experiencia=int(input("Digite os anos de experiencias: "))
if(anos_experiencia==0):
    nivel="Estágiario"
elif anos_experiencia <=3:
    nivel="Júnior" 
elif anos_experiencia <= 8:
    nivel="Pleno"
else:
    nivel="Sênior"
print(f"Você é um desenvolvedor no nível: {nivel}")  


   