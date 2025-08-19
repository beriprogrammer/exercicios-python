cliente_fiel = True
compra_acima_de_100 = False

desconto_50 = cliente_fiel or compra_acima_de_100

print(f"Cliente é fiel? {cliente_fiel}")
print(f"A compra foi acima de 100? {compra_acima_de_100}")
print(f"Tem direito a desconto? {desconto_50}")