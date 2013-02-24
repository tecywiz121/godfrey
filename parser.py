

class Parser(object):
    '''Write something here.'''
    nouns = {}
    verbs = {}

    def __init__(self, all_modules):
        '''...'''
        for module in all_modules:
            for noun in module.nouns():
                self.nouns[noun] = module
            for verb in module.verbs():
                self.verbs[verb] = module

    def parse(self, command):
        '''...'''
        pass
