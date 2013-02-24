#!/usr/env python

class Command(object):
    def __init__(self, text, noun, verb, parameters):
        self.text = text
        self.noun = noun
        self.verb = verb
        self.parameters = parameters
