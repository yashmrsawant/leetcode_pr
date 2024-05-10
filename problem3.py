"""
Given a string s, find the length of the longest 
substring
 without repeating characters.
 
Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

"""



class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        #print(s)
        m = dict()


        # Initialization
        s = s.replace(' ', '1')
        nS = len(s)
        maxLen = 0
        if nS > 0:
            i, j = 0, 0

            tkn = s[j]
            m[tkn] = 1
            j = j + 1
            maxLen = max(maxLen, j - i)

            while True:
                if j >= (nS):
                    break

                tkn = s[j]
                pr = m.get(tkn) == None

                if pr:
                    m[tkn] = 1
                    j = j + 1
                    maxLen = max(maxLen, len(m.keys()))
                    continue
                else:
                    if tkn == s[i]:
                        i = i + 1
                    else:
                        m = {}
                        m[tkn] = 1
                        maxLen = max(maxLen, len(m.keys()))
                        i = j
                    j = j + 1
        return maxLen


sol = Solution()
maxLen = sol.lengthOfLongestSubstring("ohvhjdml")
print(maxLen)