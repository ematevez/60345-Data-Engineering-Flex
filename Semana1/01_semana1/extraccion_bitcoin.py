import requests

#1. URL de destino
url = "https://data.messari.io/api/v1/assets/bitcoin/metrics"
#2. Obtener response
response = requests.get(url)
data = response.json()
results = {}
#3. Parseo JSON
results['fecha']=data['status']['timestamp']
market_data=data['data']['market_data']
results["volume_last_24_hours"]=market_data["volume_last_24_hours"]
ohlcv_24hours = market_data["ohlcv_last_24_hour"]
results['open'] = ohlcv_24hours['open']
results['low'] = ohlcv_24hours['low']
results['close'] = ohlcv_24hours['close']
results['high'] = ohlcv_24hours['high']
#4. Imprimo Resultados almacenados en dict results
print(results)