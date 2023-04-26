import requests

# Make sure to modify the .get URL with your personal API key.

class WeatherService:
    def get_temperature(self, city):
        response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=your-api-key")
        data = response.json()
        temperature = data["main"]["temp"]
        return temperature

class WeatherReporter:
    def __init__(self, service):
        self.service = service

    def report(self, city):
        temperature = self.service.get_temperature(city)
        print(f"The temperature in {city} is {temperature} degrees Celsius")

service = WeatherService()
reporter = WeatherReporter(service)
reporter.report("London")
