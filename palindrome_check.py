def isPalindrome(string):
  left = len(string) // 2
  right = left
  if len(string) % 2 == 0:
    right -= 1

  while left >= 0 and right < len(string):
    if string[left] != string[right]:
      return False
    right += 1
    left -= 1

  return True
