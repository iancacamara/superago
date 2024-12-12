import pandas as pd
from geopy.distance import geodesic

# Lista de cidades com coordenadas (latitude, longitude)
cidades_origem = {
    'São Paulo': (-23.5505, -46.6333),
    'Rio de Janeiro': (-22.9068, -43.1729),
    'Brasília': (-15.8267, -47.9218)
}

cidades_destino = {
    'Aracaju': (-10.9472, -37.0731),
    'Salvador': (-12.9714, -38.5014),
    # Adicione mais cidades destino conforme necessário
}

# Velocidade média (em km/h)
velocidade_media = 80  # Exemplo de velocidade média

# Função para calcular a distância entre duas cidades
def calcular_distancia(coord_origem, coord_destino):
    return geodesic(coord_origem, coord_destino).kilometers

# Função para calcular o tempo estimado de viagem
def calcular_tempo_viagem(distancia, velocidade_media):
    return distancia / velocidade_media

# Lista para armazenar os resultados
resultados = []

# Calcular distâncias e tempos
for origem, coord_origem in cidades_origem.items():
    for destino, coord_destino in cidades_destino.items():
        distancia = calcular_distancia(coord_origem, coord_destino)
        tempo_viagem = calcular_tempo_viagem(distancia, velocidade_media)
        resultados.append({
            'Cidade Origem': origem,
            'Coordenadas Origem': coord_origem,
            'Cidade Destino': destino,
            'Coordenadas Destino': coord_destino,
            'Distância (km)': round(distancia, 2),
            'Tempo Estimado de Viagem (horas)': round(tempo_viagem, 2)
        })

# Converter a lista de resultados em um DataFrame do pandas
df = pd.DataFrame(resultados)

# Salvar o DataFrame em um arquivo Excel
df.to_excel('rotas.xlsx', index=False)

print("As distâncias, tempos de viagem e informações das cidades foram salvas no arquivo 'rotas.xlsx'.")
