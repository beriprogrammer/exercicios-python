# 14. Realize uma operação de negação lógica em um booleano.

nome = str(input("Informe o seu nome: "))
senha = str(input("Digite sua senha: "))


if not (nome == "josé da silva e silva" and senha == "1Ae2#345@"):
    print("Nome inválido ou senha incorreta")
    email = str(input("Digite seu e-mail para reperação de login e senha: "))

    if email == "josess@Gmail":
        nome = str(input("Digite um novo nome de usuário: "))
        senha = str(input("digite uma nova senha: "))
        confirmarSenha = str(input("Repita a nova senha: "))
        if not senha == confirmarSenha:
            print("As novas senhas digitadas são diferntes")
            senha = str(input("digite uma nova senha: "))
            senha = str(input("Repita a nova senha: "))
        if senha == confirmarSenha:
            print("Atualização concluída com sucesso!")
    
    if not (email == "josess@Gmail"):
        print("E-mail não cadastrado.")