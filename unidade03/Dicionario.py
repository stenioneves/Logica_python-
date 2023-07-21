

cliente= {
    "nome":"Stenio",
    "cidade":"Duque de Caixas",
    "ano_nasc":2002 ,
    "ativo" : True
    }
print(cliente)
print(f"Cidade : {cliente['cidade']}")
print(cliente)
cliente["ano_nasc"]=int(input("Digite  ano:"))
print(cliente)
cliente.items