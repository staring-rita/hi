import requests

url = "http://api.openweathermap.org/data/2.5/weather"
api_key = "6755c93a2383e85e725d3907481596ba"

def weather(city_name):
    params = {"APPID": api_key, "q": "Новосибирск", "units": "metric", "lang": "ru"}
    result = requests.get(url, params=params)
    weather = result.json()
    print(weather)
    result = ""
    if weather['cod'] == '404':
        print('Город не найден')
    else:
        result = "в городе" + weather['name'] + '\n'
        result += "погода" + str (weather['main']['temp'])
        result += "температура" + str (weather['main']['temp'])
        result += "давление" + str (weather['main']['pressure'])
        result += "ощущается как" + str (weather['main']['fells_like'])
        result += "влажность" + str (weather['main']['humidity'])
        result += "скорость ветра" + str (weather['wind']['speed'])
        result += "восход" + str (weather['sys']['sunrise'])
        result += "закат" + str (weather['sys']['sunset'])
    #Восход sunrise
    #Закат sunset

    return result

city_name = input("введи название города: ")
data = weather(city_name)
print(data)