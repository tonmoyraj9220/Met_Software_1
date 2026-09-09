def sum_of_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

my_list = [1, 2, 3, 4, 5]

result = sum_of_list(my_list)
print("The sum of the numbers in the list is:", result)