class ITunesRateConverter(object):

	# minimum rate is 40 -> 2 stars for iTunes whereas 100 stands for 5 stars
	def __init__(self, min = 40, max = 100):
		self.__min = min
		self.__max = max
		self.__range = max - min

	def proportionalConversion(self, tracks):
		minPopularity = 10000000000
		maxPopularity = 0
		
		for track in tracks:
			if track['popularity'] > maxPopularity:
				maxPopularity = track['popularity']
			if int(track['popularity']) < minPopularity:
				minPopularity = track['popularity']

		rangePopularity = maxPopularity - minPopularity

		ratio = rangePopularity / self.__range

		for track in tracks:
			step = (track['popularity'] - minPopularity) / ratio
			track['rate'] = self.__min + step

		return True