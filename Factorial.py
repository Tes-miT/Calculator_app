num = int(input("Which number's factorial do you want? : "))
if num < 0:
    print("Entered number is invalid")
else:
    print("The 1 factorial is : 1\n")
    for i in range (2, num):
        print(f"The {i} factorial is : ", i*(i-1))
        print("")