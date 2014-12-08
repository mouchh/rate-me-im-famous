from ratefetcher import GoogleRateFetcher
from rateconverter import ITunesRateConverter
from bridge import ITunesBridge

import logging

if __name__ == '__main__':

	logging.basicConfig(
		filename = 'rate-me-im-famous.log', 
		filemode = 'w', 
		level = logging.DEBUG,
		format = '%(asctime)s - %(levelname)s - %(message)s')

	bridge = ITunesBridge()
	tracks = bridge.getTracks()

	for track in tracks:
		track['popularity'] = GoogleRateFetcher().getPopularity(track['artist'], track['song'])

	ITunesRateConverter().proportionalConversion(tracks)

	for track in tracks:
		bridge.setRate(track['itunesID'], track['rate'])

	bridge.emptyPlaylist()