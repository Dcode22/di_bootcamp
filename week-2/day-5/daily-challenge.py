#challenge 1
inputted_words = input("Enter a list of words separated by commas: ").split(',')

sortedWords = [word for word in sorted(inputted_words)]

print(sortedWords)

#challenge 2

input_sentence_words = input("Enter a sentence: ").split()

longest_word = ""

for word in input_sentence_words:
    if len(word) > len(longest_word):
        longest_word = word

print(f"The longest word is: {longest_word}")