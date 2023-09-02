
op="s"
produtos= []
while op =="s":
    nome_produto= input("Digite o nome do produto: ")
    preco_produto=float(input("Digite o preço do produto: "))
    qtd_stoque=int(input("Digite a quantidade: "))

    produto=(nome_produto,preco_produto,qtd_stoque)
    produtos.append(produto)
    op=input("Deseja cadatrar um novo produto [s/n]")

print(produto)
print(produtos)
print("Lista de produtos no estoque:")
for estoque in produtos:
    print("_______________________________")
    for produto in estoque:
        print(produto)
    print("_______________________________")    