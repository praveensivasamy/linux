""" Temperature convertors """


class TemperatureConvertors:

    def celcius_to_fahrenheit(self, value):
        result = value * (9 / 5) + 32
        print(value, "Celcius is ", result, "Fahrenheit")

    def fahrenheit_to_celcius(self, value):
        result = 5 * (value - 32) / 9
        print(value, "Fahrenheit is ", result, "Celcius")


if __name__ == "__main__":
    print("Temperature convertors")

    convertor = TemperatureConvertors()
    convertor.celcius_to_fahrenheit(23)
    convertor.fahrenheit_to_celcius(74)
