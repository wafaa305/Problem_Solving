'''Given a string s consists of some words separated by spaces, return the length of the last word in the string.
If the last word does not exist, return 0.

Constraints:
    1 <= s.length <= 104
    s consists of only English letters and spaces ' '.

The linke for this question in leetcode: https://leetcode.com/problems/length-of-last-word/
'''


'''This function takes the users string as input and is used to find the length of the last word in a string
it returns -1 if the string invalid and 0 if its a space and the length of last word if its valid'''
def find_len_last_word(string):
    if len(string)>=1 and len(string)<=10000:
        if string == ' ':
            return 0; #Return 0 if the string is a space
        else:
                string = string.strip()  # This is to remove the white-spaces from the front and back end of the string.
                list_words = list(map(str, string.split(' '))) #This to map input string into list of words
                string = string.replace(" ","")
                if string.isalpha():
                    return len(list_words[-1]) #This to find the length of last wor in the string
                else:
                    return -1 #Return -1 if the input string is not within the constraints

    else:
        return -1 #Return -1 if the input string is not within the constraints

string = input("Please enter u're string: \n")   #This to read a string from a user
len_last_word = find_len_last_word(string) #Calling the function find_len_last_word which find the length of last word in our string
#This piece of code is used to inform user with the result
if len_last_word == -1:
    print("The input string is not within the constraints")
else:
    print("The length of last word is: " + str(len_last_word))