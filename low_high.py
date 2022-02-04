entrance = input("Lowest or Highest? L/H: ")
try:
    value1 = int(input("First value: "))
    value2 = int(input("Second value: "))
    value3 = int(input("Third value: "))
except ValueError:
    print("Invalid value")
    quit()

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2 
    else:
        return num3
def low_num(num1, num2, num3):
    if num1 <= num2 and num1 <= num3:
        return num1
    elif num2 <= num1 and num2 <= num3:
        return num2
    else:
        return num3

if entrance == "L":
    res = low_num(value1,value2,value3)
    print(f"Your lowest value is: {res}")
elif entrance == "H":
    res = max_num(value1,value2,value3)
    print(f"Your highest value is: {res}")


