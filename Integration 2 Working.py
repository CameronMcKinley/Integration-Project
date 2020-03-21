#Cameron McKinley
#This program is a simple math quiz
#with a number guessing game at the end

#Imports time to be used later
import time
#imports random to be used in guessing game
import random


def main():
    print("Welcome to Cameron's quiz")
    print('Please answer all questions to the best of your ability')
    print("Lets Begin!")
    #Calls on math function to start quiz
    math()

        
def math():
    #Setting answers1-4 to 0
    answer1 = float(0)
    answer2 = float(0)
    answer3 = float(0)
    answer4 = float(0)
    #Setting answer 5 to 20 since the user will always get the last question correct
    answer5 = float(20)


    #Program pauses for 2 seconds before printing the question
    time.sleep(2)
    #Asking the first question
    question1 = int(input ("What is 12 * 9?"))
    #Checking if the user guessed correctly
    if question1 == 108:
        #Adding 25 points to the users score
        answer1 += + 20
        print("Correct!")
        #print(answer1)
    else:
        #Informing the user that their answer was incorrect
        print("Sorry, Incorrect.")

    #Program pauses for 2 seconds before printing the question
    time.sleep(2)
    #Asking the first question
    question2 = int(input ("What is 81 / 9?"))
    #Checking if the user guessed correctly
    if question2 == 9:
        #Adding 25 points to the users score
        answer2 += + 20
        print("Correct!")
        #print(answer2)
    else:
        #Informing the user that their answer was incorrect
        print("Sorry, Incorrect.")
    
    #Program pauses for 2 seconds before printing the question
    time.sleep(2)
    #Asking the first question
    question3 = int(input ("What is 25 / 2 * 12?"))
    #Checking if the user guessed correctly
    if question3 == 150:
        #Adding 25 points to the users score
        answer3 += + 20
        print("Correct!")
        #print(answer3)
    else:
        #Informing the user that their answer was incorrect
        print("Sorry, Incorrect.")


    #Program pauses for 2 seconds before printing the question
    time.sleep(2)
    #Asking the first question
    question4 = int(input ("What is 35 / 5 + 10 * 13?"))
    #Checking if the user guessed correctly
    if question4 == 137:
        #Adding 25 points to the users score
        answer4 += + 20
        print("Correct!")
        #print(answer4)
    else:
        #Informing the user that their answer was incorrect
        print("Sorry, Incorrect.")
        
    #Program pauses for 1 second before letting the user know it's the final question
    time.sleep(2)
    print("Final Question\nThis one's just for fun, unlimited attempts.")
    time.sleep(2)
    play_game()
    
    score(answer1, answer2, answer3, answer4, answer5)
    
def play_game():
    #Picks a random number between 1-100
    number = random.randint(1, 100)
    print("Guess a number between 1 and 100 inclusive.")
    #Assigns 1 to count
    count = 1
    #Loop that runs until the user guesses correctly
    while True:
        guess = int(input("Your guess: "))
        if guess > 0 and guess <= 100:
            if guess < number:
                print("Too low.")
            elif guess > number:
                print("Too high.")
            elif guess == number:
            #Prints when user guesses right along with how many attempts they made
                print("You won! You guessed it in " + str(count) + " tries.\n")
                return
            count+=1
        else:
            print("Invalid number.")
    
    
#Function to keep track of the score
def score(answer1, answer2, answer3, answer4, answer5):
    final_score = answer1 + answer2 + answer3 + answer4 + answer5
    if final_score == 100:
        print("Great job, you got a perfect score of 100!")
    elif final_score == 80:
        print("Nice, you got a score of 80.")
    elif final_score == 60:
        print("You got a score of 60, don't forget order of operations")
    elif final_score == 40:
        print("You got a score of 40, maybe you should brush up on your math")
    else:
        print("You got a score of 20, were you even trying?")
   
#Calling the main function to start the program   
main()
