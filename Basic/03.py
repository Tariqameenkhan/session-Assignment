# Guess My Number

import random 

def main():
    secret_number: int = random.randint(1, 99)
    print("I am thinking of a number between 1 and 99...")
    attemp:int=4
    user:int=0
    while user < attemp:
        print(f"rem ate {attemp-user}")
        try:
           guess = int(input("Enter a guess: "))
           user+=1
           if guess < secret_number:  
               print("Your guess is too low")
           elif guess > secret_number:
               print("Your guess is too high")
           else:    
              print("Congrats! The number was: " + str(secret_number))
              break
        except ValueError:
            print("Please enter a valid integer.")   
           
if __name__ == '__main__':
    main()