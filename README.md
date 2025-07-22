# 🌤️ Previsão do Tempo com a API da Open-Meteo

Este projeto em Python consulta a **previsão do tempo** para os próximos 7 dias usando a API gratuita da [Open-Meteo](https://open-meteo.com/), a partir do **nome de uma cidade** digitada pelo usuário. Os dados são salvos automaticamente em um arquivo `.csv`.

## 🚀 Funcionalidades

- Busca automática de **latitude, longitude e fuso horário** com base no nome da cidade.
- Consulta à API da Open-Meteo para obter:
  - Temperatura máxima (°C)
  - Temperatura mínima (°C)
  - Precipitação total (mm)
- Geração de arquivo `.csv` com a previsão dos próximos dias. (Arquivo `.csv` da cidade de Niterói usado como exemplo de resultado)

---

## 🛠️ Como usar

### 1. Clone o repositório

```bash
git clone https://github.com/eborgesfreitas/previsao_do_tempo.git

