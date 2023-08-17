import unittest

import sys
import os
# caution: path[0] is reserved for script path (or '' in REPL)
sys.path.append(os.path.dirname(os.path.abspath(__file__ + '/../')))

from sort_package.sort import Sort

class TestSort(unittest.TestCase):

    def test_swap_elements(self):
        data=[0,1,2,3,4,5,6,7,8,9]
        sorter = Sort([])
        result = sorter._Sort__swap_elements(data, 1, 4)
        self.assertEqual(result, [0,4,2,3,1,5,6,7,8,9])
        with self.assertRaises(IndexError):
            sorter._Sort__swap_elements(data, 1, 18)

    def test_select_min(self):
        data=[1,2,3,4,5,0,6,7,8,9]
        sorter = Sort([])
        result = sorter._Sort__select_min(data, 0, len(data))
        self.assertEqual(result, 5)

    def test_selection_sort(self):
        data = [3,2,1]
        sorter = Sort(data)
        result = sorter.selection_sort()
        self.assertEqual(result, [1,2,3])

    def test_find_position(self):
        data = [0,1,2,3,5,6,7,8,9]
        sorter = Sort([])
        result = sorter._Sort__find_position(data, 4)
        self.assertEqual(result, 4)

    def test_insert(self):
        data = [0,1,2,3,5,6,7,8,9]
        sorter = Sort([])
        result = sorter._Sort__insert(data, 4)
        self.assertEqual(result, [0,1,2,3,4,5,6,7,8,9])

    def test_insert_2(self):
        data = [8]
        sorter = Sort([])
        result = sorter._Sort__insert(data, 4)
        self.assertEqual(result, [4,8])

    def test_insert_3(self):
        data = [8]
        sorter = Sort([])
        result = sorter._Sort__insert(data, 14)
        self.assertEqual(result, [8,14])

    def test_insert_4(self):
        data = []
        sorter = Sort([])
        result = sorter._Sort__insert(data, 8)
        self.assertEqual(result, [8])

    def test_insertion_sort(self):
        data = [1,3,2,6,4,0,9,8,7,5]
        sorter = Sort(data)
        result = sorter.insertion_sort()
        self.assertEqual(result, [0,1,2,3,4,5,6,7,8,9])


if __name__ == '__main__':
    unittest.main()