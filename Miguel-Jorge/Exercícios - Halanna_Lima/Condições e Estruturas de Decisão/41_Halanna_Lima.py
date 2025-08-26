# Verificar se uma data informada no formato dd/mm está escrita corretamente e se existe no ano atual.

import datetime

dataFormato = str(input("Digite a data no formato : dd/mm para verificarmos: "))

try:
    dia, mes = map(int, dataFormato.split('/'))
    ano_atual = datetime.date.today().year
   
    data = datetime.date(ano_atual, mes, dia)
   
    print(f"A data {dataFormato} existe no ano de {ano_atual}.")
except ValueError:
    print(f"A data {dataFormato} não existe no calendário do ano de {ano_atual}.")
