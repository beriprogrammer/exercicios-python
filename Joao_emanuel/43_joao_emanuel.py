'''
entrada: nome de usuário e senha
processamento: verificar se a senha e o nome de usuário são iguais
saida: mensagem de erro, e voltar a pedir as informações
'''
nunca_acaba = True
while nunca_acaba:
    nome = input("Digite um nome de usuário: ")
    senha = input("Digite uma senha: ")
    if nome != senha:
     print("Processo concluído")
     break
    else:
        print("ERRO")
        print("Senha e nome de usuário não podem ser iguais!")
        print("Digite novamente!")

