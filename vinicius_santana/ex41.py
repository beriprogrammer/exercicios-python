def ano (dia, meses):
    nome_meses = {
    1: "Janeiro",
    2: "Fevereiro",
    3: "Março",
    4: "Abril",
    5: "Maio",
    6: "Junho",
    7: "Julho",
    8: "Agosto",
    9: "Setembro",
    10: "Outubro",
    11: "Novembro",
    12: "Dezembro"
    }
    dias = {
    1: 31,
    2: 28,  
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
    }
    if 1 <= meses <= 12:
       if 1 <= dia <= dias[meses]:
        print("data esta valida")
       else: 
        print("dia invalido")
    else:
     print("mes invalido")
  

    
dia, meses = map(int, input("Informe a data (dd/mm): ").split("/"))


ano(dia,meses)