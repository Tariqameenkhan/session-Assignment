# number double function

def main():
  try:
     while True:
      ver = int(input("enter your number "))
      if ver >= 100:
        return print("The number must be 99 or less. Please try again."),main()
      while ver <= 100:
        ver = ver * 2
        if ver < 100 :
         print(ver)
  except:
        print(" key error")      
        main()
if __name__ == '__main__':
    main()

# method 2
# def main():
#     while True:
#         try:
#             ver = int(input("Enter a number less than 100: "))
#             if ver >= 100:
#                 print("The number must be less than 100. Please try again.")
#                 continue
#             while ver < 100:
#                 ver *= 2
#                 if ver < 100:
#                     print(ver)
#             break
#         except ValueError:
#             print("Invalid input. Please enter a valid number.")

# if __name__ == '__main__':
#     main()
