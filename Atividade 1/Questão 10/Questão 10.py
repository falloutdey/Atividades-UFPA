#Dada uma lista de nomes, informe quais começam com a letra R.
def nomes(candidatos):
  emp = []
  for perc in candidatos:
    if perc[0] == 'R':
      emp.append(perc)
  return emp

#Exemplo de Entrada: candidatos = ['Ramon', 'Arnaldo', 'Raquel', 'Pedro', 'Rafael']
#Saída: ['Ramon', 'Raquel', 'Rafael']