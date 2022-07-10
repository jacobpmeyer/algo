import unittest

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        charPositions = {}
        longest = 0
        start = 0
        for end in range(n):
            char = s[end]
            if char in charPositions:
                start = max(start, charPositions[char])

            longest = max(longest, end - start + 1)
            charPositions[char] = end + 1
        return longest



class TestSolution(unittest.TestCase):
    def test_string1(self):
        string1 = "pwwkew"
        s = Solution()

        self.assertEqual(s.lengthOfLongestSubstring(string1), 3, "Should be 3")


    def test_string2(self):
        string2 = "abcabcbb"
        s = Solution()

        self.assertEqual(s.lengthOfLongestSubstring(string2), 3, "Should be 3")


    def test_string3(self):
        string3 = "bbbbbb"
        s = Solution()

        self.assertEqual(s.lengthOfLongestSubstring(string3), 1, "Should be 1")


    def test_string4(self):
        string4 = "dvdf"
        s = Solution()

        self.assertEqual(s.lengthOfLongestSubstring(string4), 3, "Should be 3")


if __name__ == "__main__":
    unittest.main()
