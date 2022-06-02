#Dada uma lista de sequências de bases nitrogenadas e a sequência alvo, informe a frequência de observação da sequência.
def frequencia(bases,especific):
  qntd = 0
  for perc in bases:
    if perc == especific:
      qntd = qntd + 1
  return qntd

#Exemplo de Entrada: bases = ['TACG', 'GAGC', 'ATUC', 'TAGC', 'GAGC']
#Exemplo de Sequência Alvo: especific = 'GAGC'
#Saída: 2