n = 18
number_of_guesses =  1
print("Number of guesses limited only 9 : ")
while(number_of_guesses<=9):
    guess_number = int(input("guesse the number : "))
    if guess_number<18:
        print("you enter less number ")
    elif guess_number>18:
        print("you enter greater number  ")
    else:
        print("you won")
        print(number_of_guesses , "no. of guesse you took the finish ")
        break
    print(9-number_of_guesses , "no. of guesse left")
    number_of_guesses = number_of_guesses+1
if(number_of_guesses>9):
    print("game over")

