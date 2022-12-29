#!/usr/bin/python3
"""
Calculate the values to a magnetic motor circuit (railgun)

TODO: re-organize classes and methods, this is currently very discombobulated 
TODO: add math part of claculator
TODO: debug CLI for calculator (almost complete)

"""

import sys

global flag
flag = False
# if input does contains something not from these characters, input is wrong and help will be printed
normal_characters = "FlvBIemf0123456789. " 
variables = {
    "F":"",
    "l":"",
    "v":"",
    "B":"",
    "I":"",
    "emf":""
}

help = """
MagCalc - Calculate values for a magnetic railgun circuit
usage:
    MagCalc [[variable] [value]]
Variables given will be used to solve the rest of them

Once in MagCalc, enter further values or as for all value output
show - show all values
help - show this menu
exit - quit MagCalc
<variable> <number> - variable will be changed or value added to variable"""

def quit_console():
        print(variables)
        return 0

return_statements = {
    0:None,
    1:"Input has invalid letters - here are available characters, besides numbers: FlvBIemf",

    2:"Input has too many or too little words - type \"show,\" \"help,\" or \"exit\" otherwise input should be: <variable> <value> ...",

    3:"Input contains variable that is not in variable list (F, l, v, B, I, emf)",

    "help":help, # user asks for help so help is returned

    "show":variables, # user is asking to see variables 
    # this returns the variable list, which is then parsed for output elswhere
    "exit":quit_console

}


def variable_parse(raw_user_input):
    global flag
    """
    input is a variable, followed by a number (its value)
    Removes the first variable and value in the input
    Call this recursively to read outputs
    """
    
    if (raw_user_input == "help"): return "help"
    if (raw_user_input == "show"): return "show"
    if (raw_user_input == ""): 
        flag = True # recusion is finished or user entered nothing
    
    if (flag): return 0
    
    if (type(raw_user_input) != str):
        if (type(raw_user_input) == list):
            for word in raw_user_input:
                word = word.lower()
            split_input = raw_user_input
        return "help" # user input is not a valid type
    else:
        split_input = raw_user_input.lower().split()


    # Edge case (user input contains abnormal characters)
    for character in raw_user_input:
        # find prints out the location of the character, or -1 if it does not contain.
        #   check if char is in string by evaluating if output is -1 or not
        if (normal_characters.find(character) != -1): return 1 # input is wrong and help will be printed
    
    if (len(split_input) != 2): return 2 # words are wrong (help)
    
    # first 2 words are processed (or number/anything)
    variable = split_input[0]
    value    = split_input[1]

    # everything else is sent to recurse
    output = raw_user_input[2:]
    if variable in variables:
        variables[variable] = value
    else: return 3 # variable is not in dictionary (help)
    
    variable_parse(output)




def interpret(output_code: int) -> int:
    if (output_code == 0): return None # variable assignment input, no output
    
    calculator_output = return_statements[output_code]
    if (callable(calculator_output)):
        main_loop = False
        # for quitting
    else:
        print(calculator_output)


def parse_input(user_input):
    interpret(variable_parse(user_input))
    

parse_input(sys.argv[1:])

prompt = "MagLev% "

main_loop = True
while main_loop:
    try:
        parse_input(input(prompt))
    except KeyboardInterrupt:
        # Make a clean Ctrl-C exit
        print("")
        main_loop = False


