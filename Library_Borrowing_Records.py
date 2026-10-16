
# Library Borrowing Records

books = ["Python", "Java", "C++", "AI", "DBMS"]
borrow = [4, 2, 0, 6, 2]

# 1. Average Borrow Count
total = 0

for i in borrow:
    total = total + i

average = total / len(borrow)
print("Average Borrow Count =", average)

# 2. Highest Borrowed Book
highest = borrow[0]
book_high = books[0]

for i in range(len(borrow)):
    if borrow[i] > highest:
        highest = borrow[i]
        book_high = books[i]

print("Highest Borrowed Book =", book_high)

# 3. Lowest Borrowed Book
lowest = borrow[0]
book_low = books[0]

for i in range(len(borrow)):
    if borrow[i] < lowest:
        lowest = borrow[i]
        book_low = books[i]

print("Lowest Borrowed Book =", book_low)

# 4. Count Books Not Borrowed
count = 0

for i in borrow:
    if i == 0:
        count = count + 1

print("Books Not Borrowed =", count)

# 5. Mode (Most Frequent Borrow Count)
mode = borrow[0]
max_count = 0

for i in borrow:
    c = borrow.count(i)
    if c > max_count:
        max_count = c
        mode = i

print("Mode of Borrow Count =", mode)
