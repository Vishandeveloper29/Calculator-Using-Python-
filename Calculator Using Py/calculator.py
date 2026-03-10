import os
os.system("title Calculator")

print(r"""
   ██████╗ █████╗ ██╗      ██████╗██╗   ██╗██╗      █████╗ ████████╗ ██████╗ ██████╗ 
  ██╔════╝██╔══██╗██║     ██╔════╝██║   ██║██║     ██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
  ██║     ███████║██║     ██║     ██║   ██║██║     ███████║   ██║   ██║   ██║██████╔╝
  ██║     ██╔══██║██║     ██║     ██║   ██║██║     ██╔══██║   ██║   ██║   ██║██╔══██╗
  ╚██████╗██║  ██║███████╗╚██████╗╚██████╔╝███████╗██║  ██║   ██║   ╚██████╔╝██║  ██║
   ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝
""")

first = float(input("Enter first Number : "))
operator = input("Choose Operator (+, -, *, /, %) : ")
second = float(input("Enter second Number : "))

if operator == "+":
    print("Result:", first + second)
elif operator == "-":
    print("Result:", first - second)
elif operator == "*":
    print("Result:", first * second)
elif operator == "/":
    if second == 0:
        print("Cannot divide by zero")
    else:
        print("Result:", first / second)
elif operator == "%":
    print("Result:", first % second)
else:
    print("Invalid Input")