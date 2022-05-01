import requests

api_url = "https://api.openweathermap.org/data/2.5/weather"
city = 'Chemerivtsi'  # your city

params = {
    'q' : city,
    'appid' : 'd512061b41069db8eee1cf21bc5060f8',
    'units' : 'metric'
}

result = requests.get(api_url, params=params)
data = result.json()
template = 'В місті {} зараз {} градусів'.format(city, data["main"]["temp"])
etc = 'відчувається як {} градусів \nвологість {} % \nшвидкість вітру {} м/с'.format(data["main"]["feels_like"], 
        data["main"]["humidity"], data["wind"]["speed"]) 
