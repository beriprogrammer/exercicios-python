# dados para verificação de liberação da consulta
nome = "fulano"
cpf = 12345678900
servico_selecionado = "consulta"
plano_de_saude_aceito = True
dataConsulta = True

try: # do bloco try - except para evitar que o usuário digite caracteres ou letras no campo cpf
    nome = str(input("Informe seu nome: ")).lower() # lower() torna viável tanto o uso de letras naiúsculas como o uso de minúsculas
    cpf = int(input("Digite seu CPF(apenas números): ")) 

    if nome != "fulano" or cpf != 12345678900: # condição para que seja o usuário cadastrado ainda aproveitando o bloco try - except
        print("Nome ou CPF não encontrado")
except ValueError:
    print("Tente novamente")

# validada a primeira condição, o programa entra nessa segunda condição que é uma condição com todos os elementos da vericação da consulta
    if nome == "fulano" and cpf == "12345678900" and servico_selecionado == "consulta" and plano_de_saude_aceito and dataConsulta: 
        print("Consulta liberada pelo plano de saúde.") 

else:
        print("A consulta não pode ser liberada.")

