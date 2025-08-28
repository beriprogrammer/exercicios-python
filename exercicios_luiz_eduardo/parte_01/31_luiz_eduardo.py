# Crie uma lista com strings e ordene-a em ordem alfabética decrescente.

strings = [input("Digite uma palavra: "), input("Digite outra palavra: "), input("Digite a última palavra: ")]
strings.sort(reverse=True)

print(f"Ordem alfabética decrescente: {strings}")