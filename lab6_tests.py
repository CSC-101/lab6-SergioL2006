import data
import lab6
import unittest
from data import Book

# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 0
    def test_index_smallest_from_1(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = 3
        actual = lab6.index_smallest_from(input, 0)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_2(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = 4
        actual = lab6.index_smallest_from(input, 4)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_3(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = None
        actual = lab6.index_smallest_from(input, 6)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_4(self):
        input = []
        expected = None
        actual = lab6.index_smallest_from(input, 0)
        self.assertEqual(expected, actual)


    def test_selection_sort_1(self):
        input = [1, 2, 3, 4, 5]
        expected = [1, 2, 3, 4, 5]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_2(self):
        input = []
        expected = []
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_3(self):
        input = [9, 7, 5, 3, 1]
        expected = [1, 3, 5, 7, 9]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_4(self):
        input = [5, 0, 19, 21, 4, 6]
        expected = [0, 4, 5, 6, 19, 21]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    # Part 1
    def test_part1_1(self):
        input = [Book("Morgan", "Greg"), Book("Druid", "Claw"), Book("Dray", "Gru")]
        result = lab6.selection_sort_books(input)
        check = [Book("Druid", "Claw"), Book("Morgan", "Greg"), Book("Dray", "Gru")]
        self.assertEqual(check, result)

    # Part 2
    def testpart2_1(self):
        input = "HIman"
        result = lab6.swap_case(input)
        check = "hiMAN"
        self.assertEqual(check, result)

    def testpart2_2(self):
        input = "NiÑo-HowaREyOu"
        result = lab6.swap_case(input)
        check = "nIñO-hOWAreYoU"
        self.assertEqual(check, result)
    # Part 3
    def testpart3_1(self):
        result = lab6.str_translate("rotting", "t", "b")
        check = "robbing"
        self.assertEqual(check, result)

    def testpart3_1(self):
        result = lab6.str_translate("fafsaFF", "F", "b")
        check = "fafsabb"
        self.assertEqual(check, result)
    # Part 4
    def testpart4_1(self):
        result = lab6.histogram("the word is the life of the word")
        check = {"the":3,
                 "word":2,
                 "is": 1,
                 "life":1,
                 "of":1}
        self.assertEqual(check,result)

    def testpart4_2(self):
        result = lab6.histogram("when life gives you lemons you lemons the life for more life of lemons")
        check = {"when":1,
                 "life":3,
                 "gives": 1,
                 "you":2,
                 "lemons":3,
                 "the": 1,
                 "for":1,
                 "more":1,
                 "of":1}
        self.assertEqual(check,result)


if __name__ == '__main__':
    unittest.main()
