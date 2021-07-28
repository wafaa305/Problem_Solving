'''Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
Constraints:
    1 <= strs.length <= 200
    0 <= strs[i].length <= 200
    strs[i] consists of only lower-case English letters.

The linke for this question in leetcode: https://leetcode.com/problems/longest-common-prefix/
'''


'''This function takes list of strings as input and its job is to ensure that the input strings are within the constraints'''
def is_valid_list(list_strings):
    new_list_strings = []
    if len(list_strings) >= 1 and len(list_strings) <= 200:
        for string in list_strings:
            if len(string)>=0 and len(string)<=200 and string.isalpha():
                new_list_strings.append(string.lower())
            else:
                return False
        list_strings = new_list_strings
        return True,list_strings
    return False

'''This function takes list of strings as input and its job is to find the longest common prefix  betwwen our input strings'''
def longest_common_prefix(list_strings):
    list_strings = sorted(list_strings, key=len, reverse=0) #This is to sort our strings depinding on their length in asc order
    for index in range(len(list_strings[0])):
        for element in list_strings:
            if list_strings[0][index] != element[index]:
                return list_strings[0][:index]


'''This is the main function in our program'''
def main_function():
    input_strings = input("Please enter u're string seperted by spaces:\n")   # takes the whole line of n numbers
    input_strings = input_strings.strip() #This is to remove the white-spaces from the front and back end of the input string.
    list_strings = list(map(str, input_strings.split(' '))) #This to map input strings into list of strings
    isvalid_liststrings = is_valid_list(list_strings)  #This is to ensure that the input strings are within the constraints
    is_valid = isvalid_liststrings[0]  #Map he returned values from the function is_valid_list
    list_strings = isvalid_liststrings[1]  #Map he returned values from the function is_valid_list
    longest_common_pref = ""
    longest_common_pref = longest_common_prefix(list_strings) #Finding the longest common prefix between our strings
    # This piece of code is to determine weather their is longest common prefix or not
    if longest_common_pref == "":
        print("Thier is no longest common prefix")
    else:
        print("The longest common prefix is: " + longest_common_pref)


main_function() #Calling the main function ...