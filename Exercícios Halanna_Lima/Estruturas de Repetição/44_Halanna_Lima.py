# Calcular crescimento de duas populações e descobrir em quantos anos uma supera a outra em questão de habitantes

populacaoA = 80000
populacaoB = 200000
anosAdicionados = 0

while populacaoA <= populacaoB:
    crescimentoPopulacaoA = populacaoA * (3/100)
    crescimentoPopulacaoB = populacaoB * (1.5/100)
   
    populacaoA += crescimentoPopulacaoA
    populacaoB += crescimentoPopulacaoB
    anosAdicionados += 1

print(f"Foram passados {anosAdicionados} anos até que a população A superasse a população B.")