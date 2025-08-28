# Solicita o número de termos que o usuário deseja
try:
    n = int(input("Digite o número de termos da série de Fibonacci que você deseja gerar: "))
except ValueError:
    print("Entrada inválida. Por favor, digite um número inteiro.")
    exit()

# Verifica se a entrada é válida
if n <= 0:
    print("O número de termos deve ser um número inteiro positivo.")
elif n == 1:
    print("Série de Fibonacci: 1")
else:
    # Inicializa os dois primeiros termos da série
    termo1 = 1
    termo2 = 1
    
    # Cria uma lista para armazenar a série
    fibonacci = [termo1, termo2]
    
    # Usa um loop para gerar os termos restantes
    for i in range(n - 2):
        proximo_termo = termo1 + termo2
        fibonacci.append(proximo_termo)
        
        # Atualiza os termos para a próxima iteração
        termo1 = termo2
        termo2 = proximo_termo
        
    print("Série de Fibonacci:", fibonacci)