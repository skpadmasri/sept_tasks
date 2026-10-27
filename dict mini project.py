my_dict = {}

while True:
    print()
    print("Dictionary Management System")
    print("1. Add a Word")
    print("2. Search for Meaning")
    print("3. Display All Words")
    print("4. Update Meaning")
    print("5. Delete Word")
    print("6. Exit")

    choice = int(input("Enter your choice : "))
    if choice == 1:
        word = input("Enter the word : ").lower()
        meaning = input("Enter the meaning : ").lower()
        my_dict[word] = meaning
        print("Word added successfully")
    elif choice == 2:
        word = input("Enter the word : ").lower()

        if word in my_dict:
            print("Meaning:", my_dict[word])
        else:
            print("Word not found")
    elif choice == 3:
        print(my_dict)

    elif choice == 4:
        word = input("Enter the word : ").lower()

        if word in my_dict:
            meaning = input("Enter the new meaning : ").lower()

            my_dict[word] = meaning

            print("Meaning updated successfully")
        else:
            print("Word not found")
    elif choice == 5:
        word = input("Enter the word to delete : ").lower()

        if word in my_dict:
            my_dict.pop(word)
            print("Word deleted successfully")
        else:
            print("Word not found")
    elif choice == 6:
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")