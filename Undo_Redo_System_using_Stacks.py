
# Undo/Redo System using Stacks

undo = []
redo = []
document = ""

while True:
    print("\n--- UNDO/REDO SYSTEM ---")
    print("1. Make Change")
    print("2. Undo")
    print("3. Redo")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    # Make Change
    if choice == 1:
        undo.append(document)
        document = input("Enter new text: ")
        redo.clear()
        print("Changes saved.")

    # Undo
    elif choice == 2:
        if undo:
            redo.append(document)
            document = undo.pop()
            print("Undo successful.")
        else:
            print("Nothing to undo.")

    # Redo
    elif choice == 3:
        if redo:
            undo.append(document)
            document = redo.pop()
            print("Redo successful.")
        else:
            print("Nothing to redo.")

    # Display
    elif choice == 4:
        print("Document:", document)

    # Exit
    elif choice == 5:
        print("Program terminated.")
        break

    else:
        print("Invalid choice.")
