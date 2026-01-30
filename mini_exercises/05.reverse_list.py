numbers = [1, 2, 3, 4, 5]
reversed_list = []

for num in numbers:
    reversed_list = [num] + reversed_list

print("Reversed list =", reversed_list)
