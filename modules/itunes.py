import subprocess
import module
#from response import Response
OS_WINDOWS = True
try:
    from win32com.client import Dispatch
    import win32com.client
except ImportError:
    OS_WINDOWS = False

class itunesModule(module.Module):
    ''''''
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
    		
    		#playlist = playlists(2)
    		#tracks = playlist.Tracks
    		#track = tracks.ItemByPlayOrder(2)
    		#print track.Name
    		#track.Play()
		
    @property
    def verbs(self):
        return ['play', 'shuffle']

    @property
    def nouns(self):
        return ['*']

    def can_handle(self, command):
        return (command.noun in self.nouns and command.verb in self.verbs)

    def run(self, command):
        return Response(Response.STATUS_SUCCESS)
        
