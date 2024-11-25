list = [1, 2, 3, 4]
print("List is:", list)

while True:
    print("Main menu")
    print("1. Insert")
    print("2. Delete")
    print("3. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        item = int(input("Enter item: "))
        position = int(input("In which position: "))
        index = position - 1
        list.insert(index, item)
        print("Your new list is", list)
    elif choice == 2:
        print("Deletion menu")
        print("1. Delete using value")
        print("2. Delete using index")
        print("3. Delete using sublist")

        dchoice = int(input("Enter a choice: "))
        if dchoice == 1:
            item = int(input("Item to be deleted: "))
            list.remove(item)
            print("List:", list)
        elif dchoice == 2:
            index = int(input("Index to be removed: "))
            list.pop(index)
            print("List:", list)
        elif dchoice == 3:
            low = int(input("Lower limit to be removed: "))
            high = int(input("Higher limit to be removed: "))
            del list[low:high]
            print("List:", list)
        else:
            print("Enter valid numbers")
    elif choice == 3:
        print("Program exited")
        break
    else:
        print("Valid numbers are 1, 2, 3")
