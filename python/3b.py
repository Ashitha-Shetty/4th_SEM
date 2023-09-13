def calculate_string_similarity(string1, string2):
 # Convert the strings to lowercase for case-insensitive matching
 string1 = string1.lower()
 string2 = string2.lower()
 # Calculate the similarity score
 common_chars = set(string1) & set(string2)
 similarity = len(common_chars) / max(len(string1), len(string2))
 return similarity
# Accept input from the user
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
# Call the function to calculate the similarity score
similarity_score = calculate_string_similarity(string1, string2)
# Display the result
print("The string similarity score is:", similarity_score)
