class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # counter = 0
        # iterate from the end of the str
        # if char == " " we skip
        # return counter
        counter = 0

        for char in s[::-1]:
            if char == " ":
                if counter > 0:
                    break
            else:
                counter += 1
        return counter