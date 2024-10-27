#%%

import gpxpy
import pandas as pd

#%%
# Função para ler o arquivo GPX e converter em um DataFrame do Pandas
def gpx_to_dataframe(gpx_file):
    # Abrir e ler o arquivo GPX
    with open(gpx_file, 'r') as file:
        gpx = gpxpy.parse(file)

    # Lista para armazenar os dados de cada ponto
    data = []

    # Iterar sobre os pontos do track (trilha)
    for track in gpx.tracks:
        for segment in track.segments:
            for point in segment.points:
                # Adicionar os dados do ponto à lista
                data.append({
                    'latitude': point.latitude,
                    'longitude': point.longitude,
                    'elevation': point.elevation,
                    'time': point.time
                })

    # Converter a lista em um DataFrame do Pandas
    df = pd.DataFrame(data)
    return df

# Exemplo de uso
gpx_file = 'tricolor_run.gpx'
df = gpx_to_dataframe(gpx_file)
#%%
# Exibir o DataFrame
print(df)

# %%
