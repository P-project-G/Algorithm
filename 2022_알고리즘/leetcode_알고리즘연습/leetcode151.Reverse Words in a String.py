class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        ans = " ".join(s[::-1])
        # for i in range (len(s)-1, -1, -1):
        #     ans += s[i] + " "

        return ans


# print(Solution.reverseWords(Solution,"the sky is blue"))
# print(Solution.reverseWords(Solution,"  hello world  "))

# Runtime: 56 ms, faster than 65.80% of Python3 online submissions for Reverse Words in a String.
# Memory Usage: 13.9 MB, less than 78.97% of Python3 online submissions for Reverse Words in a String.