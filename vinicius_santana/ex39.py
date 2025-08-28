def multa (km, limite):
      tolerancia = limite * 0.10
      limite_tolerado = limite + tolerancia

      if km <= limite_tolerado:
            print(f"voce esta no limite aceito {km} km/h")
      else:
            excesso =   km - limite
            porcentagem = (excesso / limite) * 100

            if porcentagem <= 20:
                print(f"voce esta {porcentagem:.2f} acima do permitido, vai levar uma multa de R$130.16 nivel media")
            elif porcentagem <= 50:
                print(f"voce esta {porcentagem:.2f} acima do permitido, vai levar uma multa de R$ 195.23 nivel grave")
            else:
                print(f"voce esta {porcentagem:.2f} acima do permitido, vai levar uma multa de R$ 880,41 nivel gravissimo")

while True:
  limite = 50
  km = int(input("informe a velocidade do carro: "))
  multa(km,limite)
  sair = input("digite S para sair ou aperte enter para continuar: ").lower()
  if sair == 's':
       break
