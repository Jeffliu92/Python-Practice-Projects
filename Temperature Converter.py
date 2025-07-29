#CONVERTE CELSIUS TO FAHRENHEIT
def celsius_to_fahrenheit(degree):
    return round((degree * 9/5) + 32, 2)

#CONVERT FAHRENHEIT TO CELSIUS
def fahrenheit_to_celsius(degree):
    return round((degree - 32) * 5/9, 2)

print(celsius_to_fahrenheit(30))
print(fahrenheit_to_celsius(92))
