def next_pelindrom(n):
    n = n+1
    while not is_pelindrom(n):
        n += 1
    return n
def is_pelindrom(n):
    return  str(n) == str(n)[::-1]

if __name__ == '__main__':
    try:
        n = int(input("Enter the number of test cases :\n"))
        numbers = []

        for i in range(n):
            number = int(input("Enter the number of the list \n"))
            numbers.append(number)
        # print(numbers)

        for i in range(n):
            print(f"next palindrom for {numbers[i]} is {next_pelindrom(numbers[i])}")
    except ValueError:
        print("plese enter integer value")
        exit()
