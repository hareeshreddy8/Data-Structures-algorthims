#https://leetcode.com/problems/valid-parentheses/
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')':'(','}':'{',']':'['}
        #let iterate through given string 
        for char in s :
            if char in mapping :
                #here through pop()we get top most element if the stack is not empty 
                top_element = stack.pop() if stack else '#'
                #here by checking the value of the curent char in mapping to the top element we can find 
                #if it is the correct closed bracket for that open bracket 
                if mapping[char] != top_element :
                    return False
            #here the char pushes into the stack if it is not in mapping 
            else :
                stack.append(char)
        
        return not stack 