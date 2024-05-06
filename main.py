import fibonacci

def main():
    print("STARTS!")
    number = int(input("Enter a number for fibonacci series: "))

    result = fibonacci.get_fabonacci_series(number)

    print(result)

main()