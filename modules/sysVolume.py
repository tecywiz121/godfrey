import subprocess
import module
import keyboard
#from response import Response

class sysVolume(module.Module):
    
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
        return (command.noun in self.nouns and command.verb in self.verbs)

    def run(self, command):
        return Response(Response.STATUS_SUCCESS)