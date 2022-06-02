#Dada a lista de conceitos de alunos de uma universidade, informe a quantidade de alunos por conceito (E – Excelente; B – Bom; R – Regular; I – Insuficiente).
def alunos(conceito):
  E= 0
  B= 0
  R= 0
  I= 0
  for perc in conceito:
    if perc == 'E':
      E = E + 1
    if perc == 'B':
      B = B + 1
    if perc == 'R':
      R = R + 1
    if perc == 'I':
      I = I + 1
  return E, B, R, I

E, B, R, I = alunos(conceito)
print(f'E =',E,
      f'B =',B,
      f'R =',R, 
      f'I =',I)

#Exemplo de Entrada: conceito = ['E', 'E', 'B', 'B', 'R', 'E', 'B', 'R', 'I', 'I', 'R', 'R', 'I']
#Saída: E = 3, B = 3, R = 4, I = 3