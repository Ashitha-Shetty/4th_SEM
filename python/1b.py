# Accept input from the user
numbers = input("Enter a list of numbers, separated by spaces: ").split()
# Convert the input values to integers
numbers = [int(num) for num in numbers]
# Calculate the sum of even numbers
even_sum = sum(num for num in numbers if num % 2 == 0)
# Output the result
print("The sum of even numbers is:", even_sum)
