]#Dada a lista da altura dos alunos de uma escola, informe qual a altura do maior aluno.
def altura(numero):
  maior = numero[0]
  for perc in numero:
    if perc > maior:
      maior = perc
  return maior

#Exemplo de entrada: numero = [1.7, 1.88. 1.5, 1.32, 1.68, 1.59]
#Saida = 1.88