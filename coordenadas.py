import pandas as pd
from geopy.distance import geodesic

# Caminhos dos arquivos
cidades_atendidas_path = r"C:\Users\IancaVieira\Clould\Supera Cloud - BU TRADE PROMO\COMPARTILHADO\IANCA CÂMARA\VS CODE\Cidades_Atendidas.xlsx"
cidades_brasil_path = r"C:\Users\IancaVieira\Clould\Supera Cloud - BU TRADE PROMO\COMPARTILHADO\IANCA CÂMARA\VS CODE\Cidades_Brasil.csv"

# Leitura dos arquivos
cidades_atendidas = pd.read_excel(cidades_atendidas_path)  # Arquivo Excel
cidades_brasil = pd.read_csv(cidades_brasil_path, sep=";", encoding="ISO-8859-1")  # Arquivo CSV com codificação correta

# Função para corrigir a coordenada (substituir vírgula por ponto, se necessário)
def corrigir_coordenada(coord):
    if isinstance(coord, str):  # Se for uma string
        return float(coord.replace(',', '.'))
    return coord  # Se já for float, retorna como está

# Função para verificar se a coordenada é válida
def coordenada_valida(coord):
    return pd.notna(coord) and coord != 0.0

# Função para calcular distância entre duas coordenadas
def calcular_distancia(cidade1, cidade2):
    # Corrigir as coordenadas
    lat1 = corrigir_coordenada(cidade1['Latitude'])
    lon1 = corrigir_coordenada(cidade1['Longitude'])
    lat2 = corrigir_coordenada(cidade2['Latitude'])
    lon2 = corrigir_coordenada(cidade2['Longitude'])
    
    # Verificar se as coordenadas são válidas
    if not (coordenada_valida(lat1) and coordenada_valida(lon1) and coordenada_valida(lat2) and coordenada_valida(lon2)):
        print(f"Coordenadas inválidas para {cidade1['Cidade']} ou {cidade2['Cidade']}")
        return None  # Retorna None para indicar erro no cálculo
    
    # Calcular e retornar a distância
    coord1 = (lat1, lon1)
    coord2 = (lat2, lon2)
    return geodesic(coord1, coord2).km

# Lista para armazenar as distâncias calculadas
distancias = []

# Calculando a distância entre todas as cidades atendidas e as cidades do Brasil
for _, cidade_atendida in cidades_atendidas.iterrows():
    print(f"Calculando distância para a cidade {cidade_atendida['Cidade']}")
    
    for _, cidade_brasil in cidades_brasil.iterrows():
        distancia = calcular_distancia(cidade_atendida, cidade_brasil)
        
        if distancia is not None:  # Ignorar caso o valor da distância seja None
            # Adicionando as distâncias ao dataframe de distâncias
            distancias.append({
                'Cidade Atendida': cidade_atendida['Cidade'],
                'Cidade Brasil': cidade_brasil['Cidade'],
                'Distancia (km)': distancia
            })

# Criando o DataFrame com as distâncias
df_distancias = pd.DataFrame(distancias)

# Verificando o número de linhas do DataFrame
print(f"Total de distâncias calculadas: {len(df_distancias)}")

# Função para dividir os dados em vários arquivos Excel, caso o limite de linhas seja excedido
def salvar_em_varios_arquivos(df, base_output_path, max_rows=1048576):
    total_rows = len(df)
    print(f"Número total de distâncias: {total_rows}")
    
    # Calcular o número de arquivos necessários para dividir
    num_files = (total_rows // max_rows) + (1 if total_rows % max_rows != 0 else 0)
    print(f"Número de arquivos necessários: {num_files}")
    
    for i in range(num_files):
        start_row = i * max_rows
        end_row = (i + 1) * max_rows  # Ajustar para garantir que não ultrapasse o limite
        
        # Verificar se o índice final está dentro do limite máximo de linhas
        if end_row > total_rows:
            end_row = total_rows
        
        print(f"Dividindo as linhas de {start_row} a {end_row-1} para o arquivo {i + 1}")
        
        output_df = df.iloc[start_row:end_row]
        output_file = f"{base_output_path}_parte_{i + 1}.xlsx"
        
        try:
            output_df.to_excel(output_file, index=False)
            print(f"Arquivo salvo: {output_file}")
        except ValueError as e:
            print(f"Erro ao salvar o arquivo {output_file}: {e}")

# Caminho de saída
output_path = r"C:\Users\IancaVieira\Clould\Supera Cloud - BU TRADE PROMO\COMPARTILHADO\IANCA CÂMARA\VS CODE\distancias"

# Salvar as distâncias em múltiplos arquivos Excel, se necessário
salvar_em_varios_arquivos(df_distancias, output_path)
