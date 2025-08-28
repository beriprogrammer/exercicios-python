#17. Realize uma operação lógica "XOR" entre dois booleanos.

boleto_por_sms = False
boleto_por_email = True

if boleto_por_sms ^ boleto_por_email: # essa proposição fica verdadeira quando uma opção é escolhida pelo usuário: a que for igual(=) a true será validada.
    
    if boleto_por_sms:  # verificando se opção por sms foi escolhida.
        print('''
        Receber boleto por SMS?
              
        Digite 1 para confirmar
        Digite 2 para cancelar''')
    elif boleto_por_email:  # verificando se opção por email foi escolhida
        print('''
        Deseja receber boleto por e-mail?
              
        Digite 1 para confirmar
        Digite 2 para cancelar''')

else: # se o usuário não escolheu nenhuma ou escolheu as duas, o else é executo: se lá em cima der false - false(duas escolhas) / true - true(nenhuma escolha).
    print("Por favor, escolha uma das opções para envio de boleto.")

'''explicando: 
1º if: escolha se quer ou boleto por sms ou boleto por email: (tem que ser true-False ou False-true acima desse if)
se true estiver no sms e o false no email, o sms será escolhido e o 2º if é acionado sendo apresentado na tela o seu print ao usuário.
se o true estiver no email e o false no sms, significa que o email foi escolhido o que aciona o elif e apresenta o seu print ao usuário.
caso o usuário não escolha nehuma opção (False na opção por sms e False na opção por email) ou escolha as duas opções(True na opção por sms e true na opção por email), o else é acionado mostrando seu print ao usuário.'''

