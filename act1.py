seceret_no = 27
attempts = 5
count = 0 
guess = 0
while count < attempts and guess != seceret_no:
    guess = int(input("Guess the Number: "))
    count = count + 1
    if guess == seceret_no:
        print("Well done You right")
        print("you have attempeted: ", count, "Number of times")
    else:
        if guess > seceret_no:
            diff = guess - seceret_no
        else:
            diff = seceret_no - guess
        if  diff >= 20:
            print("Ice Cold, Difference is too much")
        elif diff >= 10:
            print("Cold, still more to go")
        elif diff >= 5:
            print("Warm, you're closer")
        else:
            print("Hot, Too much close")
        lives = attempts - count
        print("Lives left:", end="" )
        for i in range(lives):
            print("❤️", end="")
        print("")
if guess != seceret_no:
    print("Game over All the attempts are over")
    print("Secret Number:", seceret_no )
            