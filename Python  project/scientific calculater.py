import math 
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def power(x, y):
    return x ** y

def mod(x, y):
    return x % y



print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.value of pi")
print("6.num1 power of num2")
print("7.%")
print("8.X!")
print("9.log")
print("10.squareroot")
print("11. value of sin")
print("12. value of cos")
print("13. value of tan")
print("14. Radians to Degree")
print("15. Degree to Radians")
while True:
    choice = input("Enter choice(1/2/3/4/5/6/7/8/9/10/11/12/13/14/15): ")
    if choice=="14":
        num1=eval(input("Enter Your Number: "))
        print(math.degrees(num1))
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
    if choice=="15":
        num1=eval(input("Enter Your Number: "))
        print(math.radians(num1))
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
    if choice=="5":
        print("value of pi =",math.pi)
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
    if choice=="8":
        num1 = int(input("Enter Your Number:"))
        print(num1,"! =",math.factorial(num1))
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
    if choice=="9":
        num1 = int(input("Enter your Number:"))
        print("log of",num1,"=",math.log10(num1))
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
    if choice=="10":
        num1 = float(input("Enter Your Number:"))
        print("squareroot of",num1,"=",num1**(1/2))
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
    if choice=='11':
        num1 = int(input("Enter Your Number:"))
        print("sin of",num1,"=",math.sin(math.radians(num1)))
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
    if choice=='12':
        num1 = int(input("Enter Your Number:"))
        print("cos of",num1,"=",math.cos(math.radians(num1)))
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
    if choice=='13':
        num1 = int(input("Enter Your Number:"))
        print("tan of",num1,"=",math.tan(math.radians(num1)))
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
    
    if choice in ('1', '2', '3', '4', '5', '6', '7'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))

        elif choice == '6':
            print(num1, "**", num2, "=", power(num1, num2))
        
        elif choice == '7':
            print(num1,"%",num2,"=", mod(num1, num2))
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
    
    else:
        print("Invalid Input")