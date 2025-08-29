cafe = True
acucar = True
leite = False
cafe_com_acucar = cafe and acucar
print(f"Tem café? {cafe}")
print(f"Tem açúcar? {acucar}")
print(f"Posso fazer café com açúcar? {cafe_com_acucar}") # O resultado será True

print("-" * 20)

cafe_com_leite = cafe and leite
print(f"Tem café? {cafe}")
print(f"Tem leite? {leite}")
print(f"Posso fazer café com leite? {cafe_com_leite}") # O resultado será False