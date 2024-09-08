# your code goes here!
# lib/anagram.py

class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, word_list):
        # Sort the letters of the word we're checking against
        sorted_word = sorted(self.word)
        # Filter the list for words that are anagrams of the initialized word
        return [w for w in word_list if sorted(w) == sorted_word]
