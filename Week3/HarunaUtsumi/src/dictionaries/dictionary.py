from typing import List
from abc import ABCMeta, abstractmethod


class DictionaryBase(metaclass=ABCMeta):
    def load_from_file(self, file_path: str):
        """Load the dictionary from the file

        Args:
            file_path (str): path to the source file

        Raises:
            Exception: Broken sourse file
        """
        with open(file_path) as fileobj:
            lines = [s.strip() for s in fileobj.readlines()]
            for line in lines:
                key_val = line.split("\t")
                if len(key_val) != 2:
                    raise Exception("Invalid data: " + line)
                self.insert(key_val[0], key_val[1])

    @abstractmethod
    def find(self, word: str) -> List[str]:
        """Search a word from the dictionary.

        Args:
            word (str): a word which you want to search

        Returns:
            List[str]: Return the list of the descriptions
        """
        pass

    @abstractmethod
    def find_word_by_prefix(self, prefix: str) -> List[str]:
        """Search a word using prefix from the dictionary.

        Args:
            prefix (str): a prefix which you want to search

        Returns:
            List[list]: Return the list of the words
        """
        pass

    @abstractmethod
    def insert(self, word: str, desc: str) -> bool:
        """Add a word and a description in the dictionary.

        Args:
            word (str): a word which you want to add
            desc (str): the meaning of the word

        Returns:
            bool: Return result of operation
        """
        pass

    @abstractmethod
    def delete(self, word: str, index: int) -> bool:
        """Remove a word from the dictionary.

        Args:
            word (str): a word which you want to remove
            index (int): decide which description you want to remove

        Returns:
            bool: Return result of operation
        """
        pass

    @abstractmethod
    def update(self, word: str, desc: str, index: int) -> bool:
        """Update a description in the dictionary.

        Args:
            word (str): a word which you want to remove
            desc (str): the meaning of the word which you want to change
            index (int): decide which description you want to remove

        Returns:
            bool: Return result of operation
        """
        pass

    @abstractmethod
    def save_to_file(self, filename: str):
        """Save the content of dictionary to the file

        Args:
            filename (str): a filename which you want to name
        """
        pass

    @abstractmethod
    def get_all_words(self) -> List[str]:
        """Get every words in this dictionary

        Returns:
            List[str]: Return all words
        """
        pass
