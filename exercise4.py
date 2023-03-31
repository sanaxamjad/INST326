"""
Driver: Sana Amjad, Pride Kwekam, Arshul Shaik
Navigator: Sana Amjad, Pride Kwekam, Arshul Shaik
Assignment: INST326 - Exercise 4
Date: 03_31_23

This program defines two functions: say_hello() and say_goodbye().
"""

def say_hello(name):
    """
    Takes a name as an argument and returns a greeting string.
    
    Parameters:
    name (str): The name of the person to greet.
    
    Returns:
    str: A greeting string that includes the person's name.
    """
    greeting = "Hello, " + name + "!"
    return greeting

message = say_hello("Sana")
print(message)

def say_goodbye():
    """
    Prints a goodbye message to the console.
    
    Parameters:
    None
    
    Returns:
    None
    """
    print("goodbye")

say_goodbye()
