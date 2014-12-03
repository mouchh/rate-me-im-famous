from ratefetcher import GoogleRateFetcher
from rateconverter import ITunesRateConverter
from bridge import ITunesBridge

if __name__ == '__main__':

	bridge = ITunesBridge()
	tracks = bridge.getTracks()

	for track in tracks:
		track['popularity'] = GoogleRateFetcher().getPopularity(track['artist'], track['song'])

	ITunesRateConverter().proportionalConversion(tracks)

	for track in tracks:
		bridge.setRate(track['itunesID'], track['rate'])

	bridge.emptyPlaylist()