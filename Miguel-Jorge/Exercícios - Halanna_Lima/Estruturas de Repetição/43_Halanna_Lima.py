# Pedir ao usuário o nome e uma senha e verificar se o nome é igual a senha

while True:
    nomeUsuario = str(input("Digite um nome de usuário: "))
    senhaUsuario = str(input("Agora,digite a senha do usuário: "))

    if nomeUsuario == senhaUsuario:
        print("A senha não pode ser igual ao nome de usuário, insira algo diferente!")
    else:
        print(f"Cadastro realizado com sucesso! Bem vindo(A) {nomeUsuario}")