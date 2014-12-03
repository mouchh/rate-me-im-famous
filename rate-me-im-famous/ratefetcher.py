from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import urllib
import re

class GoogleRateFetcher(object):

	def __init__(self, domain = 'fr'):
		self.__googleURL = 'https://www.google.' + domain + '/#'

	def getPopularity(self, artist, song):
		# "" are important in the query, it forces google to search the whole string rather than words
		query = {'q' : '"' + self.__cleanString(artist) + ' ' + self.__cleanString(song) + '"'}
		# headless selenium thanks to phantomJS integration
		driver = webdriver.PhantomJS()
		driver.get(self.__googleURL + urllib.urlencode(query))
		
		try:
			element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'resultStats')))
			popularity = re.findall('\d+', driver.find_element_by_id('resultStats').text.encode('utf-8').replace(' ', ''))
		finally:
			driver.quit()

		# findall return a list with one (supposed) element, we want an integer
		return int(''.join(popularity))

	# google queries are more efficient if we format a bit our artist or song string
	def __cleanString(self, string = ''):
		# first, we don't want to see what is written between (), like (feat Sting)...
		string = re.sub(r'\(.*?\)', '', string)
		# & is replaced by and
		string = string.replace('&', 'and')
		# then, everything that is not digit or alpha or whitespace is replaced with space (google doesn't search for space :))
		string = re.sub(r'[^a-zA-Z0-9\s]*', ' ', string)
		return string