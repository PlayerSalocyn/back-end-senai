class produto:
    def __init__(self,nome,preco,quantidade):
        self.nome=nome
        self.preco=preco
        self.quantidade=quantidade
    #método para saber o valor total do produto
    def valor_produto(self):
        return self.preco*self.quantidade
    def exibir_produto(self):
        print(f"""
Produto: {self.nome}
Preço: {self.preco}
Quantidade: {self.quantidade}
Valor total: {self.valor_produto()}
""")

produto1 = produto("Teclado", 150.00,10)
produto2 = produto("Monitor", 1500.00,10)

#exibir o produto
produto1.exibir_produto()
produto2.exibir_produto()
#input para armazenar os produtos em uma lista.
prod=input("Nome do produto")
preco=float(input("Preço"))
quant= float(input("Quantidade"))
produtos= produto(prod,preco,quant)
produtos.exibir_produto()
lista=[]
lista.append({"produto": prod, "Preço":preco, "quantidade": quant})
print(lista)