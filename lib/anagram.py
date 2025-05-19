# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word.lower()

    def match(self, word_list):
        # Sort the letters of the original word for comparison
        sorted_word = sorted(self.word)

        matches = []
        for candidate in word_list:
            # Normalize the candidate for case-insensitive comparison
            normalized = candidate.lower()

            # Check it's not the exact same word, and that it's an anagram
            if normalized != self.word and sorted(normalized) == sorted_word:
                matches.append(candidate)

        return matches
