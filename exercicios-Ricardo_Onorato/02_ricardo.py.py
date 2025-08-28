#2. Faça um Programa que peça as 4 notas bimestrais e mostre a média.

notas = []

nome = input("Por favor, informe o seu nome: ")

nota = float(input(f'''Olá, {nome}! Informe as 4 notas do bimestre atual: 
primeira nota: '''))
notas.append(nota)

nota = float(input(f"Segunda nota: "))
notas.append(nota)

nota = float(input(f"Terceira nota: "))
notas.append(nota)

nota = float(input(f"Quarta nota: "))
notas.append(nota)

media = sum(notas) / len(notas)
print(f'''{nome}, Sua média bimestral é:{media: .2f}''')