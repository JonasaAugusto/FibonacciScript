#Definir as variáveis
distancia = 100
vel_carro = 110
vel_caminhao = 80
tempo_pedagio_caminhao = 5/60 * 2 #(dois pedágios)

#Calcular a distância percorrida pelo carro até o cruzamento
tempo_cruzamento = distancia / (vel_carro + vel_caminhao)
dist_carro_cruzamento = vel_carro * tempo_cruzamento

#Calcular a distância restante do caminhão até Ribeirão Preto após o cruzamento
dist_restante_caminhao = distancia - dist_carro_cruzamento
tempo_caminhao_restante = dist_restante_caminhao / (vel_caminhao + (vel_caminhao*5/100)) # tempo em horas

#Comparar as distâncias finais
if dist_carro_cruzamento < dist_restante_caminhao:
  print("O carro estará mais próximo de Ribeirão Preto.")
else:
  print("O caminhão estará mais próximo de Ribeirão Preto.")
