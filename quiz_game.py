print("Welcome to my general knowledge quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("Which animal is known as the 'Ship of the Desert ")
if answer.lower() == "camel":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("How many days are there in a week? ")
if answer.lower() == "7":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("Baby frog is known as....... ")
if answer.lower() == "tadpole":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("Which animal is known as the king of the jungle? ")
if answer.lower() == "lion":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("Name the National bird of India? ")
if answer.lower() == "peacock":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("Name the National animal of India? ")
if answer.lower() == "tiger":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What type of gas is absorbed by plants? ")
if answer.lower() == "carbon dioxide":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("Who is the father of our nation? ")
if answer.lower() == "mohan das karam chandar gandhi":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What season comes after summer? ")
if answer.lower() == "autumn":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What is the largest mammal on Earth? ")
if answer.lower() == "blue whale":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 10) * 100) + "%.")
