from geopy.geocoders import Nominatim

def obter_coordenadas(cidade_estado_pais):
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode(cidade_estado_pais)
    if location:
        return (location.latitude, location.longitude)
    else:
        return None

# Teste com uma cidade
cidade = "São Paulo, SP, Brasil"
coordenadas = obter_coordenadas(cidade)

if coordenadas:
    print(f"Coordenadas de {cidade}: {coordenadas}")
else:
    print(f"Não foi possível encontrar coordenadas para {cidade}")
