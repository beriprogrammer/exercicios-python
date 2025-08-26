# Calcular quantidade de minutos gastos para pecorrer a rodovia

ComprimentoRodivia = 100
VelocidadeMedia = int(input("Insira a velocidade média que você pecorreu essa rodovia: "))
MinutosGastos = (ComprimentoRodivia / VelocidadeMedia )* 60

largura = 100
titulo =" CALCULO DE TEMPO NA RODOVIA "

print("-" * largura)
print("|" + titulo.center(largura - 2) + "|")
print("-" * largura)

print(f"|  Você gastou {MinutosGastos:.2f} para pecorrer a Rodovia numa velocidade de {VelocidadeMedia}KM/H".ljust(largura - 1) + "|")
print("-" * largura)
