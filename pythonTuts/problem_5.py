def next_pelindrom(n):
    n = n+1
    while not is_pelindrom(n):
        n += 1
    return n
def is_pelindrom(n):
    return  str(n) == str(n)[::-1]

if __name__ == '__main__':
    size = int(input("Enter the size of the lsit \n"))
    num_list = []
    for i in range(size):
        num_list.append(int(input("Enter the number of list \n")))
    print(f"you have enter {num_list}")

    print(f"output list : {[num_list[i] if num_list[i]<10 else next_pelindrom(num_list[i]) for i in range(size)] }")

    # new_list = []
    # for element in num_list:
    #     if element >10:
    #         n = next_pelindrom(element)
    #         new_list.append(n)
    #     else:
    #         new_list.append(element)
    # print(f"Output list {new_list}")
