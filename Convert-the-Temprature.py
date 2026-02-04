class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        output = []
        output.append(float(celsius + 273.15))
        output.append(float(celsius * 1.80 + 32.00))

        return output

        
