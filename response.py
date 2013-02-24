#!/usr/bin/env python

class Response(object):
    '''Contains information about the results of a command'''
    STATUS_SUCCESS = 0  # Worked!
    STATUS_OBTUSE = 1   # The module didn't understand the command
    STATUS_FAILED = 2   # The command was understood but did not work

    def __init__(self, status, message):
        self.message = message
        self.status = status
