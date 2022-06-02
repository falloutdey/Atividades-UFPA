#Dada uma lista de convidades, informe a quantidade de convidados que vão ganhar brindes, sabendo que os sorteados seriam aqueles em que o número do bilhete fosse igual a sua ordem de chegada.
def sorteio(bilhetes):
  qntd_um = 0
  qntd_dois = 0
  for perc in bilhetes:
    qntd_um = qntd_um + 1
    if perc == qntd_um:
      qntd_dois = qntd_dois + 1
  return qntd_dois

#Exemplo de Entrada: bilhetes  = [3, 2, 5, 4, 8, 6, 7, 10, 12, 13, 11]
#Saída: 5