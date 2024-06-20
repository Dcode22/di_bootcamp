class AnagramChecker:
    def __init__(self):
        with open("week-3/word_list.txt", mode="r") as word_list:
            self.word_list = word_list.read().split()

    def is_valid_word(self, word):
        if word.strip().upper() in self.word_list:
            return True
        else:
            return False


    def get_anagrams(self, word:str):
        word = word.strip().upper()
        filtered_words = [w for w in self.word_list if len(w) == len(word)]
        for l in list(set(word)):
            filtered_words = [w for w in filtered_words if word.count(l) == w.count(l)]
        anagrams = [w for w in filtered_words if word != w]
        return anagrams          
            




# checker = AnagramChecker();
# print(checker.is_valid_word(input("Enter a word to check if it is valid: ")))
# checker.get_anagrams(input('Enter a word to get all anagrams:'))