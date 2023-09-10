def is_prime(number):
 if number < 2:
    return False
 for i in range(2, int(number ** 0.5) + 1):
    if number % i == 0:
        return False
 return True
# Accept an integer from the user
num = int(input("Enter an integer: "))
# Check if the number is prime
if is_prime(num):
 print(num, "is a prime number.")
else:
 print(num, "is not a prime number.")
