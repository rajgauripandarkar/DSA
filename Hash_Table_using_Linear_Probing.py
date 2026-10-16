
# Hash Table using Linear Probing

SIZE = 10
table = [None] * SIZE


# Hash Function
def hash_function(key):
    return key % SIZE


# Insert
def insert(key):
    index = hash_function(key)

    for i in range(SIZE):
        pos = (index + i) % SIZE

        if table[pos] is None:
            table[pos] = key
            print("Key inserted.")
            return

        if table[pos] == key:
            print("Key already exists.")
            return

    print("Hash table is full.")


# Search
def search(key):
    index = hash_function(key)

    for i in range(SIZE):
        pos = (index + i) % SIZE

        if table[pos] == key:
            print("Key found at index", pos)
            return

        if table[pos] is None:
            break

    print("Key not found.")


# Delete
def delete(key):
    index = hash_function(key)

    for i in range(SIZE):
        pos = (index + i) % SIZE

        if table[pos] == key:
            table[pos] = None
            print("Key deleted.")
            return

        if table[pos] is None:
            break

    print("Key not found.")


# Display
def display():
    print("\nHash Table:")

    for i in range(SIZE):
        print(i, ":", table[i])


# Main Loop
while True:
    print("\n--- HASH TABLE ---")
    print("1. Insert")
    print("2. Search")
    print("3. Delete")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        key = int(input("Enter key: "))
        insert(key)

    elif choice == 2:
        key = int(input("Enter key to search: "))
        search(key)

    elif choice == 3:
        key = int(input("Enter key to delete: "))
        delete(key)

    elif choice == 4:
        display()

    elif choice == 5:
        print("Program terminated.")
        break

    else:
        print("Invalid choice.")
