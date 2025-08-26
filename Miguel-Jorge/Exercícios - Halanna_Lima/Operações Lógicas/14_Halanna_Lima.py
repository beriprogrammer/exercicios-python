# Receber resposta e fazer a negação dela

respostaUsuario = int(input("Olá, você gosta de sorvete? (digite 1 para sim e 0 para não): "))

if respostaUsuario == 1:
    Booleando = True
else:
    Booleando = False

if not Booleando:
    print("A negação da sua resposta é: Você gosta de sorvete")
else:
    print("A negação da sua resposta é: Você não gosta de sorvete")

