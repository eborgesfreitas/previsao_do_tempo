import requests
import pandas as pd

def get_coordinates(cidade):
    """Consulta a latitude e longitude da cidade usando a API da Open-Meteo."""
    url = f"https://geocoding-api.open-meteo.com/v1/search?name={cidade}&count=1&language=pt&format=json"
    response = requests.get(url)
    dados = response.json()

    if "results" in dados:
        dados_cidade = dados["results"][0]
        return dados_cidade["latitude"], dados_cidade["longitude"], dados_cidade["name"], dados_cidade["timezone"]
    else:
        raise Exception("Cidade não encontrada.")

def get_weather_data(latitude, longitude, timezone):
    """Consulta a previsão dos últimos 7 dias na API Open-Meteo."""
    weather_url = (
    f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}"
    f"&daily=temperature_2m_max,temperature_2m_min,precipitation_sum&timezone={timezone}&past_days=0"
    )
    response = requests.get(weather_url)
    return response.json()

def salvar_csv(weather_data, cidade):
    """Salva os dados diários em um arquivo CSV."""
    daily = weather_data['daily']
    df = pd.DataFrame(daily)
    df.to_csv(f"previsao_{cidade.lower().replace(' ', '_')}.csv", index=False)
    print(f"Arquivo 'previsao_{cidade}.csv' salvo com sucesso!")

def main():
    cidade = input("Digite o nome da cidade: ")
    try:
        lat, lon, nome_formatado, timezone = get_coordinates(cidade)
        print(f"Coordenadas {nome_formatado}: latitude {lat}, longitude {lon}")
        
        weather_data = get_weather_data(lat, lon, timezone)
        salvar_csv(weather_data, nome_formatado)
        
    except Exception as e:
        print("Erro:", e)

if __name__ == "__main__":
    main()
