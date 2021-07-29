'''Stop watch program using python threads'''


from time import *
import threading

'''This function takes the stop time as input and countdown '''
def countdown(stop_time):
    global my_timer
    my_timer = int(stop_time)
    #This piece of code is used for countdown
    for time_unit in range(my_timer):
      my_timer = my_timer - 1
      print(str(my_timer + 1) + "...")
    print("Out of Time!")

'''This is the main function in our program'''
def main_function():
    stop_time = input("Please Enter the stop time:  ")  # This to inform user ro inter the stop time
    countdown_thread = threading.Thread(target=countdown,
                                        args=(stop_time))  # Create a thread and pass the function countdown to it
    countdown_thread.start()  # Start the countdown_thread

main_function() #run our program