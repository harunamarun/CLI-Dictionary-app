from typing import List


# Edit distance
# https://en.wikipedia.org/wiki/Edit_distance
# O(n*m), n = len(word1), m = len(word2)
def _calc_edit_distance(word1: str, word2: str):
    arr = [[0 for j in range(len(word2)+1)] for i in range(len(word1)+1)]

    for i in range(len(word1)+1):
        arr[i][0] = i
    for i in range(len(word2)+1):
        arr[0][i] = i

    for i in range(1, len(word1)+1):
        for j in range(1, len(word2)+1):
            top = arr[i-1][j]
            top_left = arr[i-1][j-1]
            left = arr[i][j-1]
            if word1[i-1] == word2[j-1]:
                c = 0
            else:
                c = 1
            arr[i][j] = min(top+1, left+1, top_left+c)

    return arr[len(word1)][len(word2)]


def get_suggestions(word: str, word_list: List[str]) -> List[str]:
    """get top 5 similar words

    Args:
        word (str): a word you want to search
        word_list (List[str]): the list of candidate words

    Returns:
        List[str]: Return a list of similar words
    """
    word_distances = []
    for candidate_word in word_list:
        distance = _calc_edit_distance(word, candidate_word)
        word_distances.append((distance, candidate_word))
    word_distances.sort()
    num_suggestions = min(5, len(word_distances))
    suggested_words = [item[1] for item in word_distances[:num_suggestions]]
    return suggested_words
