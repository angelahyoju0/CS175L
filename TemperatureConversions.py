def main():
    controlLoop()

def convertToKelvin(fahrenheit):
    kelvin = (fahrenheit - 32) * 5/9 + 273.15
    return kelvin

def convertToCentigrade(fahrenheit):
    centigrade = (fahrenheit - 32) * 5/9
    return centigrade

def doConversion(fahrenheit):
    kelvin = convertToKelvin(fahrenheit)
    centigrade = convertToCentigrade(fahrenheit)
    print(f'Fahrenheit: {fahrenheit} Kelvin: {kelvin} Centigrade: {centigrade}')

def repeat():
    how_many = int(input('How many conversions would you like to do this time? '))
    for x in range(how_many):
        fahrenheit = getFahrenheit()
        doConversion(fahrenheit)

def controlLoop():
    while True:
        choice = input('Do you want to do some conversions (Yes or No)? ').lower()
        if choice == 'yes':
            repeat()
        else:
            break


def getFahrenheit():
   while True:
        fahrenheit_input = input('Enter Fahrenheit temperature (must be -50 to 130): ')
        fahrenheit = float(fahrenheit_input)
        if -50 <= fahrenheit <= 130:
            return fahrenheit
        else:
            print('Please re-enter')

if __name__ == '__main__':
    main()
