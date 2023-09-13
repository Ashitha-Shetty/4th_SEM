numbers = []
# Accept numbers from the user
while True:
 num = int(input("Enter a number (or a negative number to exit): "))
 if num < 0:
    break
 numbers.append(num)
# Calculate the sum of the numbers
total = sum(numbers)
# Display the result
print("The sum of the numbers is:", total)
