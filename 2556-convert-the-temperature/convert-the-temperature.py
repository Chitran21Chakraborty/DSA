class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        res = []
        kelvin = celsius + 273.15
        fahrenheit = celsius * 1.80 + 32.00
        res.append(kelvin)
        res.append(fahrenheit)
        return res