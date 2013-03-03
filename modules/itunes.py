import subprocess
import module
#from response import Response
OS_WINDOWS = True
try:
    from win32com.client import Dispatch
    import pythoncom
    import win32api
    import win32com.client

except ImportError:
    OS_WINDOWS = False

class itunesModule(module.Module):
    ''''''
    def winRun(self, command):
        if (command.verb in ['start, shuffle']):
            self.winShuffleAll(1)
        if (command.verb in ['next']):
            self.winNext
        if (command.verb in ['previous']):
            self.winPrevious
        if (command.verb in ['play']):
            self.winPlay
        if (command.verb in ['pause']):
            self.winPause
        if (command.verb in ['quit']):
            self.winQuit
            
    def winGetItunes(self):
        context = pythoncom.CreateBindCtx (0)
        iTunes = win32com.client.gencache.EnsureDispatch("iTunes.Application")
        for moniker in pythoncom.GetRunningObjectTable ():
            name = moniker.GetDisplayName (context, None)
            if (name == 'clsid:BBEB08F8-9126-4E20-AAD3-70B470144C72'):
                iTunes = moniker
        return iTunes
    
    def winSuffleAll(self, trackNum):
        if OS_WINDOWS:
    		iTunes = win32com.client.gencache.EnsureDispatch("iTunes.Application")
    		source = iTunes.LibrarySource
    		playlists = source.Playlists
    		
    		try:
    		    playlist = playlists(trackNum)
    		    tracks = playlist.Tracks
    		    track = tracks.ItemByPlayOrder(trackNum)
    		    print track.Name
    		    track.Play()
    		except:
    			print "Failed to play song, check iTunes for message"
    		
    def winNext(self):
        iTunes = self.winGetItunes()
        iTunes.NextTrack()
	
    def winPrevious(self):
        iTunes = self.winGetItunes()
        iTunes.PreviousTrack()
            
    def winPlay(self):
        iTunes = self.winGetItunes()
        iTunes.Play()
            
    def winPause(self):
        iTunes = self.winGetItunes()
        iTunes.Pause()

    def winQuit(self):
        iTunes = self.winGetItunes()
        iTunes.Quit()
       
#    def winMute(self):
#        iTunes = self.winGetItunes()
#        iTunes.Mute(-1)

#    def winUnMute(self):
#        iTunes = self.winGetItunes()
#        iTunes.Mute(0)
 
#    def winVolumeUp(self):
#        iTunes = self.winGetItunes()
#        volume = iTunes.SoundVolume()        
#        iTunes.SoundVolume(volume + 10)
        
#    def winVolumeDown(self):
#        iTunes = self.winGetItunes()
#        volume = iTunes.SoundVolume()        
#        iTunes.SoundVolume(volume - 10)

    @property
    def verbs(self):
        return ['play', 'pause', 'quit', 'shuffle', 'next', 'previous']

    @property
    def nouns(self):
        return ['music', 'video', 'itunes']

    def can_handle(self, command):
        return (command.noun in self.nouns and command.verb in self.verbs and self.OS_WINDOWS == true)

    def run(self, command):
        if (can_handle(command)):
            self.winRun(command)
            return Response(Response.STATUS_SUCCESS)
        else:
            return Response(Response.STATUS_FAILED)
        
