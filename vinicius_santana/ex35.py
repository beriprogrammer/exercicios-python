peso_peixe = float(input("informe quantos kg tem o peixe: "))
regulamento = 50



if peso_peixe > regulamento:
    excesso = peso_peixe - regulamento
    multa =  excesso * 4 
    print(f"""o peso  foi  alem do excedido 50 kgs  
    {excesso:.2f} a mais do limite voce vai ter que pagar r${multa:.2f}
    """)
else:
 print("peso do peixe esta no limite, parabens")
