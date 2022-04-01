import requests

def weather_app():
    country_code = input('Please enter the country code you will be using: ').upper()
    if country_code == 'US':
        city, state = input('Please enter the city and state code separated by a comma: ').split(',')
        while True:
            units = input('Please enter which units you wish to use: (imperial, metric, standard) ').lower()
            if units == 'metric' or units == 'imperial' or units == 'standard':
                break
        zip_info = str(city) + ',' + str(state) + ',' + str(country_code)
        reverse_geocode_data = {
            'q': zip_info,
            'limit': 1,
            'appid': '2312727bd558e732d4033cef3b76a40d'
        }
        location = requests.get('http://api.openweathermap.org/geo/1.0/direct', params=reverse_geocode_data)
        print(location.json())
        data = {
            'lat': location.json()[0]['lat'],
            'lon': location.json()[0]['lon'],
            'units': units,
            'appid': '2312727bd558e732d4033cef3b76a40d'
        }
        response = requests.get('https://api.openweathermap.org/data/2.5/weather', params=data)
        weather = response.json()['weather']
        temp_info = response.json()['main']

        print(weather)
        print(temp_info)

        temp = temp_info['temp']
        feels_like = temp_info['feels_like']
        temp_min = temp_info['temp_min']
        temp_max = temp_info['temp_max']
        humidity = temp_info['humidity']
        sky = weather[0]['main']
        description_sky = weather[0]['description']

        print(f'The temperature in {city}, {state} is currently: {temp} degrees fahrenheit '
              f'with a feels like temperature of: {feels_like} degrees fahrenheit. '
              f'The maximum temperature for today is going to be: {temp_max} degrees fahrenheit, '
              f'and the minimum temperature is going to be: {temp_min} degrees fahrenheit. '
              f'The humidity throughout the day today is going to be: {humidity}%. '
              f'The sky looks like it is going to be {sky} today.')
    else:
        city = input('Please enter the city: ')
        while True:
            units = input('Please enter which units you wish to use: (imperial, metric, standard) ').lower()
            if units == 'metric' or units == 'imperial' or units == 'standard':
                break
        zip_info = str(city) + ',' + str(country_code)
        reverse_geocode_data = {
            'q': zip_info,
            'limit': 1,
            'appid': '2312727bd558e732d4033cef3b76a40d'
        }
        location = requests.get('http://api.openweathermap.org/geo/1.0/direct', params=reverse_geocode_data)
        print(location.json())
        data = {
            'lat': location.json()[0]['lat'],
            'lon': location.json()[0]['lon'],
            'units': units,
            'appid': '2312727bd558e732d4033cef3b76a40d'
        }
        response = requests.get('https://api.openweathermap.org/data/2.5/weather', params=data)
        weather = response.json()['weather']
        temp_info = response.json()['main']

        print(weather)
        print(temp_info)

        temp = temp_info['temp']
        feels_like = temp_info['feels_like']
        temp_min = temp_info['temp_min']
        temp_max = temp_info['temp_max']
        humidity = temp_info['humidity']
        sky = weather[0]['main']
        description_sky = weather[0]['description']

        print(f'The temperature in {city}, {country_code} is currently: {temp} degrees fahrenheit '
              f'with a feels like temperature of: {feels_like} degrees fahrenheit. '
              f'The maximum temperature for today is going to be: {temp_max} degrees fahrenheit, '
              f'and the minimum temperature is going to be: {temp_min} degrees fahrenheit. '
              f'The humidity throughout the day today is going to be: {humidity}%. '
              f'The sky looks like it is going to be {sky} today.')


if __name__ == "__main__":
    weather_app()

