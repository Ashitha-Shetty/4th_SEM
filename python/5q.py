def filter_words_with_prefix(word_list, prefix):
 filtered_words = [word for word in word_list if word.startswith(prefix)]
 return filtered_words
# Accept input from the user
word_list = input("Enter a list of words (separated by spaces): ").split()
prefix = input("Enter the prefix to filter: ")
# Call the function to filter words
filtered_words = filter_words_with_prefix(word_list, prefix)
# Display the result
print("Filtered words:")
for word in filtered_words:
 print(word)
