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
        if (command.verb in ['play', 'shuffle']):
            self.winShuffleAll(1)
        if (command.verb in ['next', 'previous']):
            self.winNext
            
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
        if OS_WINDOWS:
            context = pythoncom.CreateBindCtx (0)
            iTunes = win32com.client.gencache.EnsureDispatch("iTunes.Application")
            for moniker in pythoncom.GetRunningObjectTable ():
                name = moniker.GetDisplayName (context, None)
                if (name == 'clsid:BBEB08F8-9126-4E20-AAD3-70B470144C72'):
                    iTunes = moniker
                print name
            iTunes.NextTrack()
	
    def winPrevious(self):
        if OS_WINDOWS:
            context = pythoncom.CreateBindCtx (0)
            iTunes = win32com.client.gencache.EnsureDispatch("iTunes.Application")
            for moniker in pythoncom.GetRunningObjectTable ():
                name = moniker.GetDisplayName (context, None)
                if (name == 'clsid:BBEB08F8-9126-4E20-AAD3-70B470144C72'):
                    iTunes = moniker
                print name
            iTunes.PreviousTrack()
	
    @property
    def verbs(self):
        return ['play', 'shuffle', 'next']

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
        
