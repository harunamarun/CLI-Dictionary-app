from typing import List
from dictionaries import DictionaryBase


class HashDictionary(DictionaryBase):
    """Dictionary implementation using hash table."""

    def __init__(self):
        self.word_to_desclist = {}

        # This is for find_word_by_prefix()
        # When this dictionary has "apple",
        # prefix_to_wordlist contains
        # {"a":[apple], "ap":[apple], "app":[apple] ... }
        self.prefix_to_wordlist = {}

    # O(1)
    def find(self, word: str) -> List[str]:
        return self.word_to_desclist.get(word, [])

    def find_word_by_prefix(self, prefix: str) -> List[str]:
        return list(self.prefix_to_wordlist.get(prefix, set()))

    # O(n) for new word, n = len(word)
    def insert(self, word: str, desc: str) -> bool:
        # Insert to word_to_desclist
        descriptions = self.word_to_desclist.get(word, [])
        descriptions.append(desc)
        self.word_to_desclist[word] = descriptions

        # Build prefix_to_wordlist
        if len(descriptions) == 1:
            for i in range(len(word)):
                prefix_length = i + 1
                prefix = word[:prefix_length]
                words = self.prefix_to_wordlist.get(prefix, set())
                words.add(word)
                self.prefix_to_wordlist[prefix] = words

        return True

    # O(n) for last desc deletion , n = len(word)
    def delete(self, word: str, index: int) -> bool:
        # Delete from word_to_desclist
        descriptions = self.word_to_desclist.get(word, [])
        if index >= len(descriptions) or index < 0:
            return False
        del descriptions[index]
        self.word_to_desclist[word] = descriptions
        if len(descriptions) == 0:
            del self.word_to_desclist[word]

        # Remove from prefix_to_wordlist
        if len(descriptions) == 0:
            for i in range(len(word)):
                prefix_length = i + 1
                prefix = word[:prefix_length]
                words = self.prefix_to_wordlist.get(prefix, set())
                words.remove(word)
                self.prefix_to_wordlist[prefix] = words

        return True

    # O(1)
    def update(self, word: str, desc: str, index: int) -> bool:
        descriptions = self.word_to_desclist.get(word, [])
        if index >= len(descriptions) or index < 0:
            return False
        descriptions[index] = desc
        self.word_to_desclist[word] = descriptions
        return True

    def save_to_file(self, filename: str):
        with open(filename, mode='w') as fileobj:
            for word, descriptions in self.word_to_desclist.items():
                for desc in descriptions:
                    fileobj.write(word + "\t" + desc + "\n")

    def get_all_words(self):
        return list(self.word_to_desclist.keys())
