#Dada uma lista de notas de alunos e a média escolar, informe quantos alunos tiveram uma nota superior a média.
def resultados(notas,media):
  qntd = 0
  for perc in notas:
    if perc > media:
      qntd = qntd + 1
  return qntd

#Exemplo de Entrada: notas = [8, 8.5, 10, 7.5, 3, 5.5, 4, 3.5]
#Exemplo de Entrada: media = 8
#Saída: 2