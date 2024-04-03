#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        dictParentheses={')':'(',']':'[','}':'{'}
        if len(s)%2!=0:
            return False
        stack=[]
        #an opening is pushed to the stack, a closing is checked against the top of the stack
        for char in s:
            if char in dictParentheses.values():
                stack.append(char)
            else:
                if stack==[] or dictParentheses[char]!=stack.pop():
                    return False
                
        return stack ==[] #if stack is empty then we have popped all the opening parentheses and found that indeed the next character is a closing parenthesis for all of them and the string is valid therefore we return True as the stack will be empty. We could have returned like this: return not stack but this is more explicit.
        
        
    
# @lc code=end

