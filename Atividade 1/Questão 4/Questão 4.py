#Dada uma lista de números, calcule a média aritmética dos números pares da lista.
def result(numeros):
  soma = 0
  qntd = 0
  media = 0
  for perc in numeros:
    if perc % 2 == 0:
      soma = soma + perc
      qntd = qntd + 1
      media = soma // qntd
  return media

#Exemplo de Entrada: numeros = [3, 5, 4, 6, 3, 2, 8, 10]
#Saída = 6
  