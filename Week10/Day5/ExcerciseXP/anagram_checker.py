class AnagramChecker:
    def __init__(self, filename):
        with open(filename, "r") as file:
            self.word_list = [word.strip().lower() for word in file.readlines()]

    def is_valid_word(self, word):
        return word.strip().lower() in self.word_list

    def is_anagram(self, word1, word2):
        return sorted(word1.strip().lower()) == sorted(word2.strip().lower())

    def get_anagrams(self, word):
        return [w for w in self.word_list if self.is_anagram(word, w) and w != word]
