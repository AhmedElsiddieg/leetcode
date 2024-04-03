#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        commonPrefix=""
        #commonPrefix can only be as long as the shortest string in the list
        if len(strs)==0:
            return commonPrefix
        for i in range(len(min(strs))):
            c=strs[0][i]
            if all(a[i]==c for a in strs[1:]):
                commonPrefix+=c
            else:
                break
        return commonPrefix
# @lc code=end

