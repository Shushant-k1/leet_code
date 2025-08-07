def UpdatedString(string):
    # Insert '#' between chars and at ends to handle even length palindromes uniformly
    newString = ['#']
    for char in string:
        newString += [char, '#']
    return ''.join(newString)

def Manacher(string):
    string = UpdatedString(string)
    LPS = [0] * len(string)
    C = R = 0
    max_len = 0  # Track max palindrome length starting at index 0
    max_center = 0

    for i in range(len(string)):
        imir = 2 * C - i
        if i < R:
            LPS[i] = min(R - i, LPS[imir])
        else:
            LPS[i] = 0

        while i + 1 + LPS[i] < len(string) and i - 1 - LPS[i] >= 0 and \
              string[i + 1 + LPS[i]] == string[i - 1 - LPS[i]]:
            LPS[i] += 1

        if i + LPS[i] > R:
            C, R = i, i + LPS[i]

        if i - LPS[i] == 0 and LPS[i] > max_len:
            max_len = LPS[i]
            max_center = i

    return max_len, max_center, string

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s:
            return s

        max_len, center, modified_str = Manacher(s)

        palindrome_prefix_len = max_len

        suffix = s[palindrome_prefix_len:]
        return suffix[::-1] + s
