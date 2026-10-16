
# Hash Table using Chaining

table = [[] for _ in range(10)]


# Insert operation
def insert(key, value):
    index = key % 10
    table[index].append((key, value))
    print("Key inserted successfully.")


# Search operation
def search(key):
    index = key % 10

    for k, v in table[index]:
        if k == key:
            print("Value:", v)
            return

    print("Key not found.")


# Delete operation
def delete(key):
    index = key % 10

    for item in table[index]:
        if item[0] == key:
            table[index].remove(item)
            print("Key deleted.")
            return

    print("Key not found.")


# Main Execution
n = int(input("Enter number of elements: "))

for i in range(n):
    key = int(input("Enter key: "))
    value = input("Enter value: ")
    insert(key, value)


# Search
key = int(input("\nEnter key to search: "))
search(key)


# Delete
key = int(input("\nEnter key to delete: "))
delete(key)


# Display Hash Table
print("\nHash Table:")

for i in range(10):
    print(i, ":", table[i])
