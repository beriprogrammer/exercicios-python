def caluladora (num1,num2,operador):

    if operador == "+":
        resultado = num1 + num2
    elif operador == "-":
        resultado = num1 - num2
    elif operador == "*":
        resultado == num1 * num2
    elif operador == "/":
        if num2 != 0:
           num1 / num2
        else:
            return"Erro: 0 nao pode ser divido"
    else:
         return"Erro: Operador inválido."
    
    return round(resultado,1)

while True:
    lista = []

    for i in range(2):
        numero = float(input("informe um numero: "))
        lista.append(numero)

    operador = input("informe um operador (-,+,*,/) ")
    
    print(caluladora(lista[0],lista[1],operador ))

    sair = input("digite s para sair ou aperte enter para continuar").lower()
    if sair == "s":

     break
    