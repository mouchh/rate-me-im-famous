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