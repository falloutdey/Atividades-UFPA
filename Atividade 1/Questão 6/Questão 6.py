#Dada a velocidade de um time de funcionários e a lista de complexidade dos itens de um pacote, informe quantos itens podem ser incluídos (A soma da complexidade dos itens incluídos deve sers menor ou igual a velocidade do time).
def itens(complex,veloc):
  soma = 0
  qntd = 0
  for perc in complex:
    soma = soma + perc
    if soma <= veloc:
      qntd = qntd + 1
  return qntd

#Exemplos de Entrada: complex = [5, 3, 4, 7, 10, 2, 3, 13, 25, 1, 1, 8]
#Exemplo de velocidade do time: veloc = 15
#Saída: 3