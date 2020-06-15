from typing import List
from dictionaries import DictionaryBase


class ListDictionary(DictionaryBase):
    """Dictionary implementation using list."""

    def __init__(self):
        self.record_list = []
    # O(n), n = number of words

    def find(self, word: str) -> List[str]:
        for record in self.record_list:
            if record["word"] == word:
                return record["desc"]
        return []

    def find_word_by_prefix(self, prefix: str) -> List[str]:
        words = []
        for record in self.record_list:
            if record["word"].startswith(prefix):
                words.append(record["word"])
        return words

    # O(n), n = number of words
    def insert(self, word: str, desc: str) -> bool:
        for record in self.record_list:
            if record["word"] == word:
                record["desc"].append(desc)
                return True
        self.record_list.append({"word": word, "desc": [desc]})
        return True

    # Worst O(n+m)
    # n = number of words
    # m = number of descriptions for target word
    def delete(self, word: str, index: int) -> bool:
        for record_index, record in enumerate(self.record_list):
            if record["word"] == word:
                if index >= len(record["desc"]) or index < 0:
                    return False
                del record["desc"][index]
                if len(record["desc"]) == 0:
                    del self.record_list[record_index]
                return True
        return False

    # O(n) n = number of words
    def update(self, word: str, desc: str, index: int) -> bool:
        for record in self.record_list:
            if index >= len(record["desc"]) or index < 0:
                return False
            if record["word"] == word:
                record["desc"][index] = desc
                return True
        return False

    def save_to_file(self, filename: str):
        with open(filename, mode='w') as fileobj:
            for record in self.record_list:
                for desc in record["desc"]:
                    fileobj.write(record["word"] + "\t" + desc + "\n")

    def get_all_words(self) -> List[str]:
        return [record["word"] for record in self.record_list]
