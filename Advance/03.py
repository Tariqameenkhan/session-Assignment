# def list_practice():
#     fruit_list = ['apple', 'banana', 'orange', 'grape', 'pineapple']
    
#     print(f"Length of the list: {len(fruit_list)}")
    
#     fruit_list.append('mango')
    
#     print(f"Updated list: {fruit_list}")

# list_practice()

def access_element(lst, index):
    if 0 <= index < len(lst):
        return f"Element at index {index}: {lst[index]}"
    else:
        return "Index out of range!"

def modify_element(lst, index, new_value):
    if 0 <= index < len(lst):
        old_value = lst[index]
        lst[index] = new_value
        return f"Modified element at index {index} from {old_value} to {new_value}"
    else:
        return "Index out of range!"

def slice_list(lst, start, end):
    if start < 0 or end > len(lst):
        return "Index out of range!"
    return lst[start:end]

def index_game():
    my_list = ['cat', 'dog', 'fish', 'bird', 'rabbit']
    print(f"Initial list: {my_list}")
    
    while True:
        print("\nSelect an operation:")
        print("1: Access an element")
        print("2: Modify an element")
        print("3: Slice the list")
        print("4: Exit")
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            try:
                index = int(input("Enter the index to access: "))
                print(access_element(my_list, index))
            except ValueError:
                print("Invalid input! Please enter an integer.")
        
        elif choice == '2':
            try:
                index = int(input("Enter the index to modify: "))
                new_value = input("Enter the new value: ")
                print(modify_element(my_list, index, new_value))
                print(f"Updated list: {my_list}")
            except ValueError:
                print("Invalid input! Please enter an integer.")
        
        elif choice == '3':
            try:
                start = int(input("Enter the start index: "))
                end = int(input("Enter the end index: "))
                result = slice_list(my_list, start, end)
                print(f"Sliced list: {result}")
            except ValueError:
                print("Invalid input! Please enter integers.")
        
        elif choice == '4':
            print("Exiting the game. Goodbye!")
            break
        
        else:
            print("Invalid choice! Please select a valid option.")

index_game()
