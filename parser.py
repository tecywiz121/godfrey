from nltk import pos_tag, word_tokenize, Tree
from nltk.parse.malt import MaltParser
from collections import defaultdict
from .command import Command

class Parser(object):
    '''Write something here.'''
    nouns = defaultdict(set)
    verbs = defaultdict(set)

    def __init__(self, all_modules, malt_working_dir=None, malt_mco=None):
        '''...'''

        if not malt_working_dir:
            import os
            malt_working_dir = os.environ['MALTPARSERHOME']

        if not malt_mco:
            malt_mco = 'engmalt.linear-1.7'

        self._parser = MaltParser(working_dir=malt_working_dir, mco=malt_mco)

        for module in all_modules:
            for noun in module.nouns:
                self.nouns[noun].add(module)
            for verb in module.verbs:
                self.verbs[verb].add(module)

    def _is_verb(self, word):
        return word in self.verbs

    def _is_noun(self, word):
        return word in self.nouns

    def _check_command(self, noun, verb):
        if not noun or not verb:
            return False
        return self.nouns[noun] & self.verbs[verb]

    def parse(self, command):
        '''...'''
        words = word_tokenize(command)
        pos = pos_tag(words)
        graph = self._parser.tagged_parse(pos)
        tree = graph.tree()

        c_noun = None
        c_verb = None

        for subtree in tree.subtrees():
            words = [x for x in subtree if not isinstance(x, Tree)] + [subtree.node]
            for x in words:
                # TODO: Use the tagged sentence so that we can resolve this better
                if self._is_verb(x):
                    c_verb = x
                elif self._is_noun(x):
                    c_noun = x
                command_modules = self._check_command(c_noun, c_verb)
                if command_modules:
                    yield Command(command, c_noun, c_verb, [])

        import code
        code.interact(local=locals())
