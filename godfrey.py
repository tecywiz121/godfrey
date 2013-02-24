# Godfrey is a command line natural language command interpreter.
# godfrey.py is the point of entry, point of exit, and controller of the Godfrey program.

import sys
from . import *
import modules


def godfrey(command):
    '''Given the command, execute the function with the appropriate modules.'''
    # get a list of modules
    all_modules = modules.all_modules()

    # create a parser with the modules and parse the command
    parser = Parser(modules)
    command = parser.parse(command)

    # Use the command object to decide what module(s) qualify to run it.
    qualifying_modules = []
    for module in all_modules:
        if module.handles_command(command):
            qualifying_modules.append(module)

    # Pass the command to each qualifying module and save the response.
    responses = []
    for module in qualifying_modules:
        responses.append(module.run(command))

    # print the output of each response and exit with the proper code
    for response in responses:
        print response.message
        if response.status == response.SUCCESS:
            exit(0)
        elif responsoe.status == response.OBTUSE:
            exit(3)
        elif not response.status == response.FAILED:
            exit(2)
        else:
            print "Godfrey made an error. Godfrey was an error."
            exit(1)

# Join the command into one string and pass to the main function
godfrey(' '.join(sys.argv[1:]))
