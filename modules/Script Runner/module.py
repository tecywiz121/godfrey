#!/usr/bin/env python

from abc import ABCMeta, abstractmethod, abstractproperty

class Module(object):
    __metaclass__ = ABCMeta

    @abstractproperty
    def verbs(self):
        '''Returns an iterable object of the verbs that this module supports'''
        raise NotImplemented

    @abstractproperty
    def nouns(self):
        '''Returns an iterable object of the nouns that this module supports'''
        raise NotImplemented

    @abstractmethod
    def can_handle(self, command):
        '''Returns True if this module can handle this type of a command.

        :param command: A command to test
        :type verb: str
        :returns: bool -- True if this module handles this command'''
        raise NotImplemented
