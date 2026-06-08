import random 
import math 
class smart_bot:
    def __init__(self,min=1,max=10):
        self.min_range = min
        self.max_range = max
        self.counter = 0
        self.memory = {}
        self.unique_shield = set()

    def  generate_random_number(self):
        while True:
            guess = random.randint(self.min_range,self.max_range)
            if guess not in self.unique_shield:
                self.counter += 1

            self.memory[self.counter] = guess
            self.unique_shield.add(guess)   
            return guess
    def update_range(self,feedback):
        if feedback == "too low":
            self.min_range = self.memory[self.counter] + 1
        elif feedback == "too high":
            self.max_range = self.memory[self.counter] - 1


if __name__ == "__main__":
    secret_number = random.randint(1,10)
    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 10. Can you guess it?")
    bot = smart_bot(min=1,max=10)   
    while True:
        guess = bot.generate_random_number()
        print(f"Bot's guess: {guess}")
        if guess < secret_number:
            print("Too low!")
            bot.update_range("too low")
        elif guess > secret_number:
            print("Too high!")
            bot.update_range("too high")
        else:
            print(f"Congratulations! The bot guessed the number {secret_number} in {bot.counter} attempts!")
            break


        
       