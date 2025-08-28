#15. Realize uma operação lógica "E" entre dois booleanos.

nome = "nomeCadastrado"
senha = "senha_cadastrada"
plano_de_saude_aceito = True
dataConsulta = True

nome = str(input("Digite seu nome: ")).lower() # .lower() converte todos os caracteres de uma string para minúsculo
senha = str(input("Digite sua senha: "))

if nome != "nomeCadastrado".lower() or senha != "senha_cadastrada":
    print("Nome incorreto ou senha invalida.")

elif plano_de_saude_aceito and dataConsulta:       # operação lógica "E" entre dois booleanos.
    print("Consulta liberada pelo plano de saúde.")
    
else:
    print("Consulta não liberada.")