class WeatherForecast():
    def __init__(self, temperatures):
        self.temperatures = temperatures

    @staticmethod 
    def convert_from_fahrenheit_to_celsius(fahr):
        calculation = (5/9) * (fahr - 32)
        return round(calculation, 2)

    def in_celsius(self):
        return [self.convert_from_fahrenheit_to_celsius(temp) for temp in self.temperatures]

wf = WeatherForecast([100, 90, 80, 70, 60])
print(wf.in_celsius()) #

print(WeatherForecast.convert_from_fahrenheit_to_celsius(100))