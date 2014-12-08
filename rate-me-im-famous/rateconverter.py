import logging

class ITunesRateConverter(object):

	# minimum rate is 40 -> 2 stars for iTunes whereas 100 stands for 5 stars
	def __init__(self, min = 40, max = 100):
		logging.info('ITunesRateConverter creation...')
		self.__min = min
		self.__max = max
		self.__range = max - min
		logging.info('ITunesRateConverter created.')

	def proportionalConversion(self, tracks):
		logging.info('Begining of proportional rate conversion...')
		minPopularity = 10000000000
		maxPopularity = 0
		
		for track in tracks:
			if track['popularity'] > maxPopularity:
				maxPopularity = track['popularity']
			if int(track['popularity']) < minPopularity:
				minPopularity = track['popularity']

		rangePopularity = maxPopularity - minPopularity

		ratio = rangePopularity / self.__range

		logging.debug('maxPopularity %s', maxPopularity)
		logging.debug('minPopularity %s', minPopularity)
		logging.debug('rangePopularity %s', rangePopularity)
		logging.debug('ratio %s', ratio)

		for track in tracks:
			step = (track['popularity'] - minPopularity) / ratio
			track['rate'] = self.__min + step
			logging.debug('track %s', track)

		logging.info('Conversion done.')
		return True