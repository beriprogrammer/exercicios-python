# 18. Realize uma operação lógica "NÃO" exclusiva em um booleano.

# Enquanto as boias subirem(true) juntas ou descerem(false) juntas, quer dizer que o sistema(boias e bomba) está funcionando se qualquer uma parar o sistema para apresentará defeito e para de funcionar.
boiaA_sobe = False
boiaB_sobe = False

bomba_hidraulica_funcionando = not (boiaA_sobe ^ boiaB_sobe)

if bomba_hidraulica_funcionando:
  print("em funcionamento")
else:
  print("com defeito.")