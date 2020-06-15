from utils.suggest import _calc_edit_distance
import unittest


class TestSuggest(unittest.TestCase):
    def test_calc_edit_distance(self):
        self.assertEqual(1, _calc_edit_distance("apple", "applo"))
        self.assertEqual(2, _calc_edit_distance("apple", "apploo"))
        self.assertEqual(2, _calc_edit_distance("apple", "app"))
        self.assertEqual(5, _calc_edit_distance("apple", ""))
        self.assertEqual(5, _calc_edit_distance("aaaaa", "zzzzz"))


if __name__ == '__main__':
    unittest.main()
