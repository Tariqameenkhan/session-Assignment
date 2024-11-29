# JOKE funcion

PROMPT: str = "What do you want? "
JOKE: str = "Here is a joke  he he he eh ! "
SORRY: str = "Sorry I only tell jokes."

def main():
    
    user_input = input(PROMPT)
    user_input = user_input.strip().lower()
    # try:   
    if "joke" in user_input:
            print(JOKE)
    else:
            print(SORRY)
    return main() #"loop again for input"
    # except :
    #     print("error")


if __name__ == "__main__":
    main()