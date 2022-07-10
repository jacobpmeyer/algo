class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        keys = {}
        for i, char in enumerate(s):
            if keys.get(char) is None:
                keys[char] = []
                keys[i] = []
            keys[char].append(i)
            firstIdx = keys[char][0]
            keys[firstIdx].append(i)

        longest = 1
        for key, arr in keys.items():
            arr.append(len(s) - 1)
            if type(key) == str or len(arr) == 1:
                next
            i = 0
            while i < len(arr) - 1:
                unbroken = True
                for j in range(arr[i], arr[i + 1]):
                    # can't have more than one apearance between the two being checked
                    startCheck, endCheck = arr[i], arr[i + 1]
                    if keys.get(j) is not None:
                        count = 1
                        for pos in keys[j]:
                            if pos > startCheck and pos < endCheck:
                                count += 1
                        if count > 1:
                            unbroken = False
                            break

                if unbroken is True:
                    currentRun = arr[i + 1] - arr[i] + 1
                    if currentRun > longest:
                        if arr[i + 1] == len(s) - 1 and s[arr[i]] != s[arr[i + 1]]:
                            print(arr[i], arr[i + 1])
                            currentRun += 1
                        # print(arr[i], arr[i + 1])
                        longest = currentRun

                i += 1

        return longest

string1 = "pwwkew"
string2 = "abcabcbb"
string3 = "bbbbbb"
string4 = "dvdf"
s = Solution()
print(s.lengthOfLongestSubstring(string1)) #=> 3
print(s.lengthOfLongestSubstring(string2)) #=> 3
print(s.lengthOfLongestSubstring(string3)) #=> 1
print(s.lengthOfLongestSubstring(string4)) #=> 3
