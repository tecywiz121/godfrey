#!/usr/bin/env python
from datetime import datetime
import module
from response import Response

class TimeModule(module.Module):

    @property
    def verbs(self):
        '''Returns an iterable object of the verbs that this module supports'''
        return ['is']

    @property
    def nouns(self):
        '''Returns an iterable object of the nouns that this module supports'''
        return ['time']

    def can_handle(self, command):
        '''Returns True if this module can handle this type of a command.

        :param command: A command to test
        :type verb: str
        :returns: bool -- True if this module handles this command'''
        return True # TODO: fix this

    def run(self, command):
        '''Execute a command'''
        return Response(Response.STATUS_SUCCESS, unicode(datetime.now()))
