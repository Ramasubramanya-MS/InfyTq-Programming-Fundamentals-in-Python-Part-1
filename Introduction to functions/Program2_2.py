#program to covert degree in fahrenheit to celsius
f_deg = float(1)
def celsiusto_fahrenheit(f_deg):#f_deg refers to degree in Fahrenheit
    c_deg = (f_deg-32)*(5/9) #c_deg refers to degree in celsius
    return c_deg

degree_celsius = celsiusto_fahrenheit(98)
print(degree_celsius)
