
# Customer Account ID Search

# Store customer account IDs in a list
ids = [125, 240, 365, 480, 595]

# Take customer ID from the user
key = int(input("Enter Customer ID: "))

# --------- Linear Search ---------
found_linear = False

for id in ids:
    if id == key:
        found_linear = True
        break

if found_linear:
    print("Linear Search: ID Found")
else:
    print("Linear Search: ID Not Found")


# --------- Binary Search ---------
low = 0
high = len(ids) - 1
found_binary = False

while low <= high:
    mid = (low + high) // 2

    if ids[mid] == key:
        found_binary = True
        break
    elif ids[mid] < key:
        low = mid + 1
    else:
        high = mid - 1

# Display Binary Search result
if found_binary:
    print("Binary Search: ID Found")
else:
    print("Binary Search: ID Not Found")
