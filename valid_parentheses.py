'''Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.

Constraints:
    1 <= s.length <= 10^4
    s consists of parentheses only '()[]{}'.

The linke for this question in leetcode: https://leetcode.com/problems/valid-parentheses/
'''

#This function takes the uer string as input and check if its wthin constraint or not
def is_valid_string(string):
    if len(string) >= 1 and len(string) <= 10000:
        for char in string:
            if char != "(" and char != ")" and char != "{" and char != "}" and char != "[" and char != "]":
                return False
        return True
    return False

#This function tkes user's string as input and check if its contains valid parentheses or not
def is_valid_parentheses(string):
    stack = []
    for parenthese in string:
        if parenthese == "(" or parenthese == "[" or parenthese == "{":
            stack.append(parenthese)
        else:
            top = stack.pop()
            if parenthese == ")" and top == "(" or parenthese == "]" and top == "[" or parenthese == "}" and top == "{":
               continue

            else:
                return "Invalid Parentheses"

    if len(stack) == 0:
        return "Valid Parentheses"
    return "Invalid Parentheses"

string = input("Please Enter a string of parentheses: \n")
is_valid_str = is_valid_string(string) #Check if string is within contraints

#This piecee of code is to call the function is_valid_parentheses if the string is within the contraints
if is_valid_str == True:
    is_valid = is_valid_parentheses(string)
    print("Res: "+ is_valid)
else:
    print("Invalid Input: should contain only parentheses...")
