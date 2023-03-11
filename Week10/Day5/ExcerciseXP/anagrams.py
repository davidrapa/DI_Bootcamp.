from anagram_checker import AnagramChecker


def validate_word(word):
    if not word.isalpha():
        return False


    if len(word.split()) != 1:
        return False

    return True


def get_user_input():
    user_input = input("Please enter a word (or 'exit' to quit): ")
    user_input = user_input.strip()


    if user_input.lower() == "exit":
        return None


    if not validate_word(user_input):
        print("Invalid input. Please enter a single word containing only alphabetic characters.")
        return get_user_input()

    return user_input.lower()


def display_results(word, anagrams):
    if not anagrams:
        print(f"No anagrams found for {word}.")
    else:
        print(f"Your word: {word}\nThis is a valid English word.\nAnagrams for your word: {', '.join(anagrams)}.\n")


if __name__ == "__main__":
    anagram_checker = AnagramChecker("word_list.txt")
    while True:
        user_input = get_user_input()
        if not user_input:
            break

        if anagram_checker.is_valid_word(user_input):
            anagrams = anagram_checker.get_anagrams(user_input)
            display_results(user_input, anagrams)
        else:
            print(f"{user_input} is not a valid English word.")

