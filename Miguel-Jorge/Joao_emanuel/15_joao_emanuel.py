posicao_valida = True
bola_entrou = True

gol_valido = bola_entrou and posicao_valida
print(f"A bola entrou?{bola_entrou}")
print(f"A posição foi válida? {posicao_valida}")
print(f"Então o goi foi validado? {gol_valido}")