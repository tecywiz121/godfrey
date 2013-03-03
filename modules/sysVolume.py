import subprocess
import module
import keyboard
#from response import Response
import os

class sysVolume(module.Module):
    
    def winRun(command):
        if (command.verb in ['turn up', 'up']):
            self.winVolumeUp
        if (command.verb in ['turn down', 'down']):
            self.winVolumeDown
    
    def winVolumeUp(self):
        myKeyboard = keyboard.keyboardCommand()
        print 'Pressing the volume up button'
        for x in range(1, 10):
            myKeyboard.winPressKey('volume_up')
        
    def winVolumeDown(self):
        myKeyboard = keyboard.keyboardCommand()
        print 'Pressing the volume up button'
        for x in range(1, 10):
            myKeyboard.winPressKey('volume_down')
        
	#def volumeDown(self):
        
        
    #def volumeUp(self):
        
	
    @property
    def verbs(self):
        return ['turn up', 'up', 'turn down', 'down']

    @property
    def nouns(self):
        return ['volume']

    def can_handle(self, command):
        return (command.noun in self.nouns and command.verb in self.verbs and os.name == 'nt')

    def run(self, command):
        if (can_handle(command)):
            self.winRun(command)
            return Response(Response.STATUS_SUCCESS)
        else:
            return Response(Response.STATUS_FAILED)