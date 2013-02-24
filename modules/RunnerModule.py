import subprocess
import module

class RunnerModule(module.Module):
    '''modulePath: path to the module, arg: parameters to pass'''
    def winRunner(self, modulePath, arg):

        print 'Runner.py started'
        print 'Running program:', str(modulePath), 'with arguements:', str(arg)
        subprocess.call(["C:\Python27\python.exe", modulePath, arg])

    def runner(self, modulePath, arg):

        print 'Runner.py started'
        print 'Running program:', str(modulePath), 'with arguements:', str(arg)
        subprocess.call([modulePath, arg])

    @property
    def verbs(self):
        return ['run', 'open']

    @property
    def nouns(self):
        return ['file']

    def can_handle(self, command):
        return (command.noun in self.nouns and command.verb in self.verbs)

    def run(self, command):
        subprocess.call([command.noun])
