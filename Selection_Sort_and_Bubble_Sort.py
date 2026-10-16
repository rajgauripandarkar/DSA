
salaries = [50000.5, 30000.5, 80000.5,
            45000.5, 90000.5, 60000.5, 40000.5]

# Selection Sort
a = salaries.copy()

for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if a[i] > a[j]:
            a[i], a[j] = a[j], a[i]

print("Selection Sort:", a)

# Bubble Sort
b = salaries.copy()

for i in range(len(b)):
    for j in range(len(b) - 1):
        if b[j] > b[j + 1]:
            b[j], b[j + 1] = b[j + 1], b[j]

print("Bubble Sort:", b)

# Top 5 Highest Salaries
print("Top 5 Salaries:", b[-5:][::-1])
