def tempreature():
     
     Fahrenheit = int(input("Enter temperature in Fahrenheit: "))
     Last_fahrenheit = (Fahrenheit -32)  * 5.0/9.0
     print(f"Temperature: {Last_fahrenheit}C")


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    tempreature()