#შექნენით ფუნქცია რომელიც გადააქცევს celsius fahrenheit-ად (პირიქითაც შეგიძლიათ)
def celsius_to_fahrenheit(value):
    return (value * 9/5) + 32

def fahrenheit_to_celsius(value):
    return (value - 32) * 5/9

def temperature_converter(value, scale):
    scale = scale.lower()
    if scale == 'celsius':
        return celsius_to_fahrenheit(value)
    elif scale == 'fahrenheit':
        return fahrenheit_to_celsius(value)
    return "Error: Scale must be 'celsius' or 'fahrenheit'"

print(temperature_converter(25, 'celsius'))  
print(temperature_converter(77, 'fahrenheit')) 
print(temperature_converter(100, 'kelvin'))  