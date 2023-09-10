def find_maximum(numbers):
 if not numbers:
    raise ValueError("The list is empty.")
 maximum = numbers[0] # Initialize maximum with the first element
 for num in numbers:
     if num > maximum:
        maximum = num
     return maximum
# Call the function with a list of numbers and store the result in a variable
numbers = [1, 40, 2, 88, 3]
max_num = find_maximum(numbers)
# Print the result
print("The maximum number is:", max_num)
