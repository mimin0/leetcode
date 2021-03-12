class Solution:
    def reverse(self, x: int) -> int:
        newString = str(abs(x))
        newString = newString.strip()

        reversedNewString = newString[::-1]

        output = int(reversedNewString)

        if output >= 2 ** 31 - 1 or output <= -2 ** 31:
            return 0
        elif x < 0:
            return -1 * output
        else:
            return output
