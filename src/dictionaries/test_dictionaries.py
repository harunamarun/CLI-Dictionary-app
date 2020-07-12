from dictionaries import TrieDictionary, ListDictionary, HashDictionary

import unittest


class TestDictionaries(unittest.TestCase):
    def setUp(self):
        self.dictionaries = [
            TrieDictionary(), ListDictionary(), HashDictionary()]

        for dictionary in self.dictionaries:
            dictionary.insert("mer", "cari")

    def test_insert_find(self):
        for dictionary in self.dictionaries:
            with self.subTest(dictionary=dictionary):
                self.assertEqual(["cari"], dictionary.find("mer"))

    def test_insert_multiple_desc(self):
        for dictionary in self.dictionaries:
            with self.subTest(dictionary=dictionary):
                dictionary.insert("mer", "caricari")
                self.assertEqual(["cari", "caricari"], dictionary.find("mer"))

    def test_find_noExist(self):
        for dictionary in self.dictionaries:
            with self.subTest(dictionary=dictionary):
                self.assertEqual([], dictionary.find("merucari"))

    def test_find_word_by_prefix(self):
        for dictionary in self.dictionaries:
            with self.subTest(dictionary=dictionary):
                dictionary.insert("mario", "my older brother")
                dictionary.insert("mercari", "mercari mercari")
                self.assertEqual({"mercari", "mer"},
                                 set(dictionary.find_word_by_prefix("me")))
                self.assertEqual({"mario", "mercari", "mer"},
                                 set(dictionary.find_word_by_prefix("m")))

    def test_delete(self):
        for dictionary in self.dictionaries:
            with self.subTest(dictionary=dictionary):
                dictionary.insert("merca", "ri")
                self.assertTrue(dictionary.delete("mer", 0))
                self.assertEqual([], dictionary.find("mer"))
                self.assertEqual(["ri"], dictionary.find("merca"))
                self.assertTrue(dictionary.delete("merca", 0))
                self.assertEqual([], dictionary.find("merca"))

    def test_delete_invalid(self):
        for dictionary in self.dictionaries:
            with self.subTest(dictionary=dictionary):
                self.assertFalse(dictionary.delete("mercari", 0))
                self.assertFalse(dictionary.delete("mer", 1))
                self.assertFalse(dictionary.delete("mer", -1))
                self.assertTrue(dictionary.delete("mer", 0))

    def test_update(self):
        for dictionary in self.dictionaries:
            with self.subTest(dictionary=dictionary):
                self.assertTrue(dictionary.update("mer", "caricari", 0))
                self.assertEqual(["caricari"], dictionary.find("mer"))

    def test_update_invalid(self):
        for dictionary in self.dictionaries:
            with self.subTest(dictionary=dictionary):
                self.assertFalse(dictionary.update("mooooo", "caricari", 0))
                self.assertFalse(dictionary.update("mer", "caricari", 1))
                self.assertFalse(dictionary.update("mer", "caricari", -1))
                self.assertTrue(dictionary.update("mer", "caricari", 0))

    def test_get_all_words(self):
        for dictionary in self.dictionaries:
            with self.subTest(dictionary=dictionary):
                dictionary.insert("mercari", "carucaru")
                self.assertEqual({"mer", "mercari"},
                                 set(dictionary.get_all_words()))
                dictionary.delete("mercari", 0)
                self.assertEqual({"mer"}, set(dictionary.get_all_words()))

    def test_save_and_load(self):
        for dictionary in self.dictionaries:
            with self.subTest(dictionary=dictionary):
                dictionary.save_to_file("test.txt")
                dictionary.load_from_file("test.txt")
                self.assertEqual({"mer"}, set(dictionary.get_all_words()))

    def test_non_ascii(self):
        for dictionary in self.dictionaries:
            with self.subTest(dictionary=dictionary):
                dictionary.insert("メルカリ", "めるかり")
                self.assertEqual(["めるかり"], dictionary.find("メルカリ"))
                dictionary.insert("★", "りんごStar")
                self.assertEqual(["りんごStar"], dictionary.find("★"))
                self.assertEqual(
                    ["★"], dictionary.find_word_by_prefix(""))
                self.assertEqual({"★", "mer", "メルカリ"},
                                 set(dictionary.get_all_words()))


if __name__ == '__main__':
    unittest.main()
