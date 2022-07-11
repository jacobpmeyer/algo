from re import I


class Solution:
    def maxArea(self, height: list[int]) -> int:

        # return "You fucking suck and you are never going to be anything"



s = Solution()
import unittest
class TestSolution(unittest.TestCase):
    def test_49(self):
        arr = [1,6,8,6,2,5,4,8,3,7]
        self.assertEqual(s.maxArea(arr), 49, "Should be 49")

    def test_0(self):
        arr = [0, 2]
        self.assertEqual(s.maxArea(arr), 0, "Should be 0")

    def test_1(self):
        arr = [1,1]
        self.assertEqual(s.maxArea(arr), 1, "Should be 1")

    def test_8(self):
        arr = [1,0,0,0,0,0,0,2,2]
        self.assertEqual(s.maxArea(arr), 8, "Should be 8")

    def test_4(self):
        arr = [1,2,4,3]
        self.assertEqual(s.maxArea(arr), 4, "Should be 4")


if __name__ == "__main__":
    unittest.main()
