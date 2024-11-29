import random

class HighLowGame:
    def __init__(self, num_rounds=5):
        self.num_rounds = num_rounds  
        self.score = 0 

    def play_round(self, round_number):
        print(f"Round {round_number}")
        
        player_number = random.randint(1, 100)
        computer_number = random.randint(1, 100)
        
        print(f"Your number is {player_number}")
        
        guess = input("Do you think your number is higher or lower than the computer's? (Press Enter to quit): ").strip().lower()
        if not guess: 
            return False
        
        while guess not in {"higher", "lower"}:
            guess = input("Please enter either higher or lower (or press Enter to quit): ").strip().lower()
            if not guess:  
                return False
        
        if player_number > computer_number and guess == "higher":
            print("You were right!", end=" ")
            self.score += 1
        elif player_number < computer_number and guess == "lower":
            print("You were right!", end=" ")
            self.score += 1
        else:
            print("Aww, that's incorrect.", end=" ")
        
        print(f"The computer's number was {computer_number}")
        print(f"Your score is now {self.score}")
        # print()  
        return True  

    def play_game(self):
        print("Welcome to the High-Low Game!")
        print("--------------------------------")
        
        for round_number in range(1, self.num_rounds + 1):
            if not self.play_round(round_number):  
                print("\nYou exited the game early!")
                break 
        
        if self.score > 0 or round_number == self.num_rounds:
            print("\nThanks for playing!")
            if self.score == self.num_rounds:
                print("Wow! You played perfectly!")
            elif self.score >= self.num_rounds // 2:
                print("Good job, you played really well!")
            else:
                print("Better luck next time!")
        
        input("\nPress Enter to close the game...")
              

h1=HighLowGame(5)
h1.play_game()
