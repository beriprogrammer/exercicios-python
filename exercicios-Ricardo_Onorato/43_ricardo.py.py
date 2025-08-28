# 43. Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

# O loop vai rodar indefinidamente até que a condição de saída seja satisfeita
while True:
    usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")
    
    # Compara a senha com o nome de usuário
    if senha == usuario:
        # Se forem iguais, exibe uma mensagem de erro
        print("Erro: A senha não pode ser igual ao nome de usuário. Tente novamente.")
    else:
        # Se forem diferentes, exibe uma mensagem de sucesso e sai do loop
        print("Usuário e senha registrados com sucesso!")
        break