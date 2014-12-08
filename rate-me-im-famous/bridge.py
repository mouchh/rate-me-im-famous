from ScriptingBridge import SBApplication, NSPredicate

import logging

class ITunesBridge(object):

	def __init__(self, library = 'Library', playlist = 'Rate Me Im Famous'):
		logging.info('ITunesBridge creation...')
		self.__iTunes = SBApplication.applicationWithBundleIdentifier_('com.apple.iTunes')
		self.__library = self.__iTunes.sources().objectWithName_(library)
		self.__playlist = self.__library.playlists().objectWithName_(playlist)
		logging.info('ITunesBridge created.')

	def getTracks(self):
		logging.info('Retrieving tracks...')
		data = []
		for track in self.__playlist.tracks():
			data.append({'artist' : track.artist(), 'song' : track.name(), 'itunesID' : track.id()})
		logging.info('Tracks retrieved.')
		logging.debug('tracks %s', data)
		return data

	def setRate(self, songID, rate):
		logging.info('Setting rate %s for song with ID %s', rate, songID)
		self.__playlist.tracks().objectWithID_(songID).setRating_(rate)
		logging.info('Rate given.')
		return True

	def emptyPlaylist(self):
		logging.info('Cleaning the playlist...')
		properties = {'name': self.__playlist.name()}
		logging.debug('properties %s', properties)
		# delete old playlist
		self.__playlist.delete()

		# adding new empty playlist with the same old name
		# applescript defines 'playlist' class, so we should be able to create a new playlist instance using the scripting bridge
		newPlaylist = self.__iTunes.classForScriptingClass_('playlist').alloc().initWithProperties_(properties)
		self.__library.playlists().insertObject_atIndex_(newPlaylist, 0)

		# recreating link
		self.__playlist = self.__library.playlists().objectWithName_(properties['name'])
		logging.info('Playlist cleaned')
		return True


