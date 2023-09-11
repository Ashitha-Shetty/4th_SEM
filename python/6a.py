import string
def count_words(input_file, output_file):
 word_count = {}
 
 # Read input file and count occurrences of each word
 with open(input_file, 'r') as file:
    for line in file:
 # Remove punctuation and convert to lowercase
        line = line.translate(str.maketrans('', '', string.punctuation))
 line = line.lower()
 
 # Split the line into words
 words = line.split()
 
 # Count the occurrences of each word
 for word in words:
    if word in word_count:
        word_count[word] += 1
 else:
    word_count[word] = 1
 
 # Write word count results to the output file
 with open(output_file, 'w') as file:
    for word, count in word_count.items():
        file.write(f"{word}: {count}\n")
# Usage example
input_file = "input.txt"
output_file = "output.txt"
count_words(input_file, output_file)