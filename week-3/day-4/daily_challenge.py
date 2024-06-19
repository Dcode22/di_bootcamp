import re
class Text:
    def __init__(self, text:str):
        self.text = text
        pattern = r"[^a-zA-Z']+"
        self.clean_text = re.sub(pattern, " ", self.text.lower())
        self.clean_text = re.sub(r'\s+', ' ', self.clean_text)

    def from_file(self, file_path: str):
        with open(file_path, mode='r') as file:
            self.text = file.read()
            pattern = r"[^a-zA-Z']+"
            self.clean_text = re.sub(pattern, " ", self.text.lower())
            self.clean_text = re.sub(r'\s+', ' ', self.clean_text).strip()
            return self

    def word_frequency(self, word: str):
        count = self.clean_text.split().count(word)
        if not count:
            print(f"The word '{word}' is not found in the text")
        else: 
            print(f"The word '{word}' is found {count} times in the text")
        return self.clean_text.count(word)
    
    def unique_words(self):
        return sorted(list(set([word for word in self.clean_text.split(' ') if word])))
    
    def most_common_word(self):
        highest_count = 0
        most_common_word = None
        for word in self.unique_words():
            count = self.clean_text.count(word)
            if count == highest_count:
                if isinstance(most_common_word, list):
                    most_common_word.append(word)
                else: 
                    most_common_word = [most_common_word, word]

            elif count > highest_count:
                highest_count = count
                most_common_word = word

        return most_common_word     

def analyze_text():
    new_text = Text(input("Enter text to analyze: "))    
    query = input("Enter a word to find how often it is found in the text:")
    new_text.word_frequency(query)     
    print("Here are all the unique words in the text:")
    print(new_text.unique_words())
    most_common_word =  new_text.most_common_word()
    if isinstance(most_common_word, list):
        print(f"{', '.join([f"'{word}'" for word in most_common_word[:-1]])} and  '{most_common_word[-1]}' are tied for most common word.")
    else: 
        print(f"The most common word is '{most_common_word}'")
        
    
def analyze_file():
    file_path = input("Enter a file path to analyze the text in the file: ")
    file_text = Text("").from_file(file_path)
    query = input("Enter a word to find how often it is found in the file:")
    file_text.word_frequency(query)         
    print("Here are all the unique words in the file:")
    print(file_text.unique_words())
    most_common_word =  file_text.most_common_word()
    if isinstance(most_common_word, list):
        print(f"{', '.join([f"'{word}'" for word in most_common_word[:-1]])} and  '{most_common_word[-1]}' are tied for most common word.")
    else: 
        print(f"The most common word is '{most_common_word}'")

analyze_text()
analyze_file()