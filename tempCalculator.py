def main():
    num = int(input ("Enter the temperature, number only: "))
    temp = input("Celsius or Fahrenheit?: ")

#if-elif-else not working, only printing if statement
    if (temp == "Celsius" or temp == "celsius" or temp == 'C' or temp == 'c'):
        print("The temperature is: " + celsiusConverter(temp, num) + " degrees Fahrenheit")
    elif (temp == "Fahrenheit" or temp == "fahrenheit" or temp == 'F' or temp == 'f'):
        print("The temperature is: " + fahrenheitConverter(temp, num) + " degrees Celsius")
    else:
        print("Temperature must be Celsius or Fahrenheit, C or c, F or f.")


def celsiusConverter (t, n):
    if (t == "Celsius" or t == "celsius" or t == 'C' or t == 'c'):
        newTemp = n * (9/5) + 32
        newTemp = format(newTemp, '.2f')
        newTemp = str(newTemp)
        return newTemp

def fahrenheitConverter (t, n):
    if (t == "Fahrenheit" or t == "fahrenheit" or t == 'F' or t == 'f'):
        newTemp = ((n - 32)) * (5/9)
        newTemp = format(newTemp, '.2f')
        newTemp = str(newTemp)
        return newTemp
main()






# def kelvinConverter
#    if (temp = "Kelvin" or "kelvin" or 'K' or 'k'):
#       newTemp =