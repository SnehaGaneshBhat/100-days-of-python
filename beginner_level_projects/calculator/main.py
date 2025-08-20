import art
print(art.logo)
result = 0

def add(n1, n2):
    return (n1 + n2)

def sub(n1,n2):
    return n1 - n2

def mul(n1,n2):
    return n1 * n2

def div(n1,n2):
    return n1 / n2

operation = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div,
}

def calculate():
    n1 = int(input("Whats the first number?: "))
    should_calculate = True
    while should_calculate:
        print(" + \n - \n * \n / \n")
        op = input("Pick an operation: ")
        n2 = int(input("Whats the next number?: "))
        result = (operation[op](n1, n2))
        print(f"{n1} {op} {n2} = {result}")
        stay = input("Enter y to continue with operations. Enter n to move on to new operations").lower()
        if stay == 'y':
            num1 = result
        else:
            should_calculate = False
            print("\n" *20)
            calculate()


calculate()

















