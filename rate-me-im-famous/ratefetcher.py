from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# used in url encoding
import urllib

# used to extract number from the content string in the resultStat div from google
import re

class GoogleRateFetcher(object):

	def __init__(self, domain = 'fr'):
		self.__googleURL = 'https://www.google.' + domain + '/#'

	def getPopularity(self, artist, song):
		query = {'q' : '"' + artist + ' ' + song + '"'}

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