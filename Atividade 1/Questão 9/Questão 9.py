#Dado uma lista de vulnerabilidades de softwares, informe quantos softwares estão em cada classe de segurança. (0 - Muito seguro, Entre 1 e 3 - Seguro, Entre 4 e 5 - Quase Seguro, Mais de 5 - Inseguro).
def seguranca(vulnerability):
  MS = 0
  S = 0
  QS = 0
  I = 0
  for x in vulnerability:
    if x == 0:
      MS = MS + 1
    if x >= 1 and x <= 3:
      S = S + 1
    if x >= 4 and x <= 5:
      QS = QS + 1
    if x > 5:
      I = I + 1
  return MS, S, QS, I

MS, S, QS, I = seguranca(vulnerability)
print(f'Muito seguro:',MS)
print(f'Seguro:',S)
print(f'Quase seguro:',QS)
print(f'Inseguro:',I)

#Exemplo de Entrada: vulnerability = [0, 0 ,1, 3, 2, 4, 5, 6, 1, 2, 7]
#Saída: Muito seguro: 2  Seguro: 5  Quase seguro: 2  Inseguro: 2