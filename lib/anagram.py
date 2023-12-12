class Anagram:
    def __init__(self, word):
        self.word = word.lower()  

    def match(self, word_list):
        return [word for word in word_list if self.is_anagram(word)]

    def is_anagram(self, other_word):
        other_word_lower = other_word.lower()
        
        
        return self.word != other_word_lower and sorted(self.word) == sorted(other_word_lower)
