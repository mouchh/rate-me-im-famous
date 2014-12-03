from ScriptingBridge import SBApplication, NSPredicate

class ITunesBridge(object):

	def __init__(self, library = 'Library', playlist = 'Rate Me Im Famous'):
		self.__iTunes = SBApplication.applicationWithBundleIdentifier_('com.apple.iTunes')
		self.__library = self.__iTunes.sources().objectWithName_(library)
		self.__playlist = self.__library.playlists().objectWithName_(playlist)

	def getTracks(self):
		data = []
		for track in self.__playlist.tracks():
			data.append({'artist' : track.artist(), 'song' : track.name(), 'itunesID' : track.id()})
		return data

	def setRate(self, songID, rate):
		self.__playlist.tracks().objectWithID_(songID).setRating_(rate)
		return True

	def emptyPlaylist(self):
		properties = {'name': self.__playlist.name()}

		# delete old playlist
		self.__playlist.delete()

		# adding new empty playlist with the same old name
		# applescript defines 'playlist' class, so we should be able to create a new playlist instance using the scripting bridge
		newPlaylist = self.__iTunes.classForScriptingClass_('playlist').alloc().initWithProperties_(properties)
		self.__library.playlists().insertObject_atIndex_(newPlaylist, 0)

		# recreating link
		self.__playlist = self.__library.playlists().objectWithName_(properties['name'])
		return True


