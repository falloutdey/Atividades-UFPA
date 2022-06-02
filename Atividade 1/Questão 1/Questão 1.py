#Dada uma lista de tamanho de embalagens, retorne quantas embalagens estão fora do padrão (Menores que 7, não são aceitas)
def embalagens(tamanho):
  qntd = 0
  for perc in tamanho:
    if perc < 7:
      qntd = qntd + 1
  return qntd 

#Exemplo de entrada: tamanho = [3,5,8,2,11,1,4,4,4,4]
#Saída = 8