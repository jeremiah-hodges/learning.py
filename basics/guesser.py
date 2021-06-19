
secret = "zebra"
guess = ""
count = 1
limit = 3

while guess != secret:
    guess = input("Enter in a guess: ")
    if count == limit:
        print("Out of guesses, you loose!")
        break
    elif guess == secret:
        print(print("You won in " + str(count) + " guesses!"))
        break
    count += 1

