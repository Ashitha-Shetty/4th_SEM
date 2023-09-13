def count_word_occurrences(sentence, word):
 # Convert the sentence and word to lowercase for case-insensitive matching
 sentence = sentence.lower()
 word = word.lower()
 # Split the sentence into individual words
 words = sentence.split()
 # Count the occurrences of the word in the sentence
 count = words.count(word)
 return count
# Accept input from the user
sentence = input("Enter a sentence: ")
word = input("Enter the word to search for: ")
# Call the function and get the count of word occurrences
occurrences = count_word_occurrences(sentence, word)
# Display the result
print("The word",word,"occurs",occurrences, "times in the sentence.")
