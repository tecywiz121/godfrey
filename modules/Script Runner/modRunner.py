import subprocess
import module

class RunFile(module.Module):
    '''modulePath: path to the module, arg: parameters to pass'''
    def winRunner(self, modulePath, arg):

        print 'Runner.py started'
        print 'Running program:', str(modulePath), 'with arguements:', str(arg)
        subprocess.call(["C:\Python27\python.exe", modulePath, arg])
	
    def runner(self, modulePath, arg):

        print 'Runner.py started'
        print 'Running program:', str(modulePath), 'with arguements:', str(arg)
        subprocess.call([modulePath, arg])

    def verbs(self):
        return ['run', 'open']

    def nouns(self):
        return ['file']

    def can_handle(self, command):
        return (command.noun in nouns() and verbs.verb in verbs())