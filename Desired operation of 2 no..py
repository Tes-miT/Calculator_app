a = int(input("PLease enter your 1st number : "))
b = int(input("PLease enter your 2nd number : "))
op = input("Please the operator you want : ")
if op == "+":
    print("Your result is =", a+b)
if op == "-":
    print("Your result is =", a-b)
if op == "*":
    print("Your result is =", a*b)
if op == "/":
    print("Your result is =", a/b)
else:
    print("Invalid operator")