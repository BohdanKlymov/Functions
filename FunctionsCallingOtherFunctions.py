def fahrenheit_to_celsius(fahrenheit):

    celsium = fahrenheit / 32
    return celsium

def weather_report():
    fahrenheit = 124
    print(f"The temperature is {format(fahrenheit_to_celsius(fahrenheit), '.1f')}°C")

weather_report()