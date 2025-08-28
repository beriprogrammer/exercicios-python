# 41. Faça um Programa que peça uma data no formato dd/mm e determine se a mesma é uma data válida para o ano atual.

from datetime import datetime # datetime(biblioteca) possui todas as regras de calendário (meses, anos bissextos, etc.) integradas.

data = input("Digite uma data no formato dd/mm: ")

ano_atual = datetime.now().year # Pega o ano atual do sistema.
data_completa = f"{data}/{ano_atual}" # Concatena a entrada do usuário com o ano atual para formar uma string de data completa.

try:
    # Tenta converter a string para um objeto de data
    datetime.strptime(data_completa, '%d/%m/%Y') #  Este método tenta "analisar" a string data_completa_str de acordo com o formato %d/%m/%Y.
    
    print("Data válida!")
except ValueError:
    print("Data inválida. Por favor, use o formato dd/mm.")

# dentro do bloco try - except:
# - Se a string corresponder a uma data real e válida, o método strptime funciona e o programa segue.
# - Se a string não for uma data válida (por exemplo, 31/02, 13/01), o strptime levanta um erro ValueError, que é capturado pelo except, exibindo a mensagem "Data inválida".