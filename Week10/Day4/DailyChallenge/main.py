class Text:
    def __init__(self, text):
        self.text = text

    def word_frequency(self, word):
        words = self.text.split()
        freq = words.count(word)
        if freq == 0:
            return f"The word '{word}' does not appear in the text."
        else:
            return f"The word '{word}' appears {freq} times in the text."

    def most_common_word(self):
        words = self.text.split()
        counts = {}
        for word in words:
            if word in counts:
                counts[word] += 1
            else:
                counts[word] = 1
        return max(counts, key=counts.get)

    def unique_words(self):
        words = self.text.split()
        return list(set(words))

    @classmethod
    def from_file(cls, filename):
        with open(filename, "r") as file:
            text = file.read()
        return cls(text)


# Testing with a simple string
simple_text = "A good book would sometimes cost as much as a good house."
text_obj = Text(simple_text)
print(text_obj.word_frequency("good"))
print(text_obj.most_common_word())
print(text_obj.unique_words())

# Testing with an external text file
file_text_obj = Text.from_file("the_stranger.txt")
print(file_text_obj.word_frequency("the"))
print(file_text_obj.most_common_word())
print(file_text_obj.unique_words())
