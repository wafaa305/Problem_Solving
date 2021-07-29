'''Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times.
You may assume that the majority element always exists in the array.

The linke for this question in leetcode: https://leetcode.com/problems/majority-element/
'''
import math

'''This function takes list of numbers as input and is used to find the element that appears more than ⌊n / 2⌋ times'''
def find_majority_element(list_numbers):
    map = {}
    #Theis piece of code is to map the element and its number of repetitions into dectionary (we used hash map method
    for number in list_numbers:
        if number not in map:
            map[number] = 0
            map[number] += 1
        else:
            map[number] += 1

    # Consider the first element as the maximum element
    max_element_key=list(map.keys())[0]
    max_element_value = map[max_element_key]

    #This to find the element  that appears more than ⌊n / 2⌋ times
    for key,value in map.items():
        if value > max_element_value:
            max_element_value = value
            max_element_key = key
        else:
            continue
    return max_element_key,max_element_value

'''This is the main function in our program'''
def main_process():
    numbers = input("Please enter you're numbers seperated by spaces")
    list_numbers = list(map(int, numbers.split(' '))) #This to map input numbers into list of numbers
    majority_element,nums_of_rep = find_majority_element(list_numbers) #Call the function find_majority_element to find the majority element

    #This piece of code is to enre that the majority element i repeted more than ⌊n / 2⌋ times
    if nums_of_rep >= math.floor(len(list_numbers)/2):
        print(majority_element)
    else:
        print("There is no majority element ...")

main_process()