def celsius_to_fahrenheit():
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

print (celsius_to_fahrenheit(),"ºF")