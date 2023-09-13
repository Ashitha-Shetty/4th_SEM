def count_word_frequencies(sentence):
 # Convert the sentence to lowercase and split into words
 words = sentence.lower().split()
 # Create an empty dictionary to store word frequencies
 frequencies = {}
 # Count the frequencies of each word
 for word in words:
    if word in frequencies:
        frequencies[word] += 1
    else:
        frequencies[word] = 1
 return frequencies
# Accept input from the user
sentence = input("Enter a sentence: ")
# Call the function to count word frequencies
word_frequencies = count_word_frequencies(sentence)
# Display the result
print("Word frequencies:")
for word, frequency in word_frequencies.items():
 print(word, ":", frequency)