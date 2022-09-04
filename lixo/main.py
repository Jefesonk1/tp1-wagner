import numpy as np
import math
np.set_printoptions(suppress=True)

def deslocamento(cx, cy):
  return np.array([[1,0,cx], [0,1,cy],[0,0,1]])

def escalonamento(sx, sy):
  return np.array([[sx,0,0],[0,sy,0],[0,0,1]])

def rotacao(grau):
  return np.array([[math.cos(math.radians(grau)), -math.sin(math.radians(grau)), 0],[math.sin(math.radians(grau)), math.cos(math.radians(grau)),0],[0,0,1]])

p1 = (700,400)
p2 = (1700,400)
p3 = (1700,1150)
p4 = (700,1150)

lista_pontos_janela = [(700,400), (1700,400), (1700,1150), (700,1150)]
lista_pontos_janela_deslocado = []

for ponto in lista_pontos_janela:
  ponto_deslocado = np.matmul(deslocamento(-700,-400), np.array([*ponto,1]))
  print(ponto_deslocado)
  lista_pontos_janela_deslocado.append(ponto_deslocado)

print('\n\n')
for ponto in lista_pontos_janela_deslocado:
  rotado = np.matmul(rotacao(30),ponto)
  rotado_final = np.matmul(deslocamento(500, 100), rotado)
  print(rotado_final[:-1])