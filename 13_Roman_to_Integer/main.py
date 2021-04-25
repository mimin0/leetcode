class Solution:
    def romanToInt(s: str):

        mapping = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        n = len(s)
        total = mapping[s[n - 1]]
        for i in range(n - 1, 0, -1):
            current = mapping[s[i]]
            prev = mapping[s[i - 1]]
            total += prev if prev >= current else -prev
        return total


test = Solution

for numeral, expected in [['CLXIV', 164], ['MDCCLXXXIII', 1783], ['XIV', 14]]:
    assert test.romanToInt(numeral) == expected
