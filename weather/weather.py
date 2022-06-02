import requests

API_KEY = '86953e24421168c10db0bf2593e70f16'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

city = input('Enter city name: ')
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']

    temperature = round(data['main']['temp'] - 273.15, 2)
    print("The weather:", weather)
    print("Temperature today: ", temperature, 'celsius')
else:
    print('An error occurred while requesting weather')
