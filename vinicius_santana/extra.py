def calculcador (num1,num2,operador):

    if operador == "-":
        resultado = num1 - num2
    elif operador == "+":
        resultado = num1 + num2
    elif operador == "*":
        resultado = num1 * num2
    elif operador ==  "/":
          if num2 != 0:
            resultado = num1 / num2
          else: 
            return "Erro: 0 nao pode ser dividido"
    else:
        return "Erro: Operador inválido."
    return round(resultado, 1)


for j in range(100):

 lista = []

 for i in range(2):
    x = float(input("informe o numero: "))
    lista.append(x)

 operador=input("insira um operador (-,+,*,/) ")

 print(calculcador(lista[0],lista[1], operador)) 

 sair = input("digite s para sair: ").lower()
 if sair == 's':
    
   break





