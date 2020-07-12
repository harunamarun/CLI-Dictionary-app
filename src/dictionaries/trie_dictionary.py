from typing import List, TextIO
from dictionaries import DictionaryBase


class TrieNode:
    def __init__(self):
        self.word = None
        self.children = {}
        self.desc = []


class TrieDictionary(DictionaryBase):
    """Dictionary implementation using trie tree."""

    def __init__(self):
        self.head = TrieNode()

    # O(n), n = len(word)
    def find(self, word: str) -> List[str]:
        return self._find(self.head, word, 0)

    def _find(self, node: TrieNode, word: str, depth: int) -> List[str]:
        if depth == len(word):
            return node.desc

        char = word[depth]
        if char in node.children:
            return self._find(node.children[char], word, depth+1)
        else:
            return []

    def find_word_by_prefix(self, prefix: str) -> List[str]:
        return self._find_word_by_prefix(self.head, prefix, 0)

    def _find_word_by_prefix(self, node: TrieNode, prefix: str,
                             depth: int) -> List[str]:
        if depth < len(prefix):
            char = prefix[depth]
            if char not in node.children:
                return []
            return self._find_word_by_prefix(node.children[char],
                                             prefix, depth+1)
        else:
            words = []
            for char in node.children:
                children_words = self._find_word_by_prefix(node.children[char],
                                                           prefix, depth+1)
                words.extend(children_words)
            if node.word:
                words.append(node.word)
            return words

    # O(n), n = len(word)
    def insert(self, word: str, desc: str) -> bool:
        return self._insert(self.head, word, desc, 0)

    def _insert(self, node: TrieNode, word: str, description: str,
                depth: int) -> bool:
        if depth == len(word):
            node.word = word
            node.desc.append(description)
            return True

        char = word[depth]
        if char not in node.children:
            node.children[char] = TrieNode()
        return self._insert(node.children[char], word, description, depth+1)

    # O(n), n = len(word)
    def delete(self, word: str, index: int) -> bool:
        ret = self._delete(self.head, word, 0, index)
        return ret["op_status"]

    def _delete(self, node: TrieNode, word: str, depth: int,
                index: int) -> dict:
        if depth == len(word):
            if index >= len(node.desc) or index < 0:
                return {"op_status": False, "delete_me": False}
            del node.desc[index]
            if not node.desc:
                node.word = None
            if node.children or node.desc:
                return {"op_status": True, "delete_me": False}
            else:
                return {"op_status": True, "delete_me": True}

        char = word[depth]
        if char not in node.children:
            return {"op_status": False, "delete_me": False}
        ret = self._delete(node.children[char], word, depth+1, index)
        if ret["delete_me"]:
            del node.children[char]
            if not node.children and not node.desc:
                return {"op_status": ret["op_status"], "delete_me": True}
        return {"op_status": ret["op_status"], "delete_me": False}

    # O(n), n = len(word)
    def update(self, word: str, desc: str, index: int) -> bool:
        return self._update(self.head, word, desc, 0, index)

    def _update(self, node: TrieNode, word: str, description: str, depth: int,
                index: int) -> bool:
        if depth == len(word):
            if index >= len(node.desc) or index < 0:
                return False
            node.desc[index] = description
            return True

        char = word[depth]
        if char not in node.children:
            return False
        return self._update(node.children[char], word, description, depth+1,
                            index)

    def save_to_file(self, filename: str):
        with open(filename, mode='w') as fileobj:
            self._save_to_file(self.head, fileobj)

    def _save_to_file(self, node: TrieNode, fileobj: TextIO):
        if node.word and node.desc:
            for desc in node.desc:
                fileobj.write(node.word + "\t" + desc + "\n")

        for char in node.children:
            self._save_to_file(node.children[char], fileobj)

    def get_all_words(self) -> List[str]:
        return self._get_all_words(self.head)

    def _get_all_words(self, node: TrieNode) -> List[str]:
        words = []
        for char in node.children:
            children_words = self._get_all_words(node.children[char])
            words.extend(children_words)
        if node.word:
            words.append(node.word)
        return words
