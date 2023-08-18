# calculator ==> with yes or no option

def calculate():
    number_1 = int(input("please enter your first number : "))
    number_2 = int(input("please enter your second number : "))

    operation = input('''
    + for addition
    - for subtraction
    * for multiplication
    / for division
    ''')
    if operation == "+":
        out_put = number_1 + number_2
        print("{} + {} = {}".format(number_1,number_2,out_put))
    elif operation == "-":
        out_put = number_1 - number_2
        print("{} - {} = {}".format(number_1,number_2,out_put))
    elif operation == "*":
        out_put = number_1 - number_2
        print("{} * {} = {}".format(number_1,number_2,out_put))
    elif operation == "/":
        out_put = number_1 - number_2
        print("{} / {} = {}".format(number_1,number_2,out_put))
    else:
        print("sorry your input is wrong ): ")
    again()

def again():
    calc_again=input("Do you like to continue ? (y/n) ")
    if calc_again.upper() == "Y":
        calculate()
    elif calc_again.upper() == "N":
        print("see you later :) ")

calculate()