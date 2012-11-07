import urllib2
import re
import argparse
from BeautifulSoup import BeautifulSoup 
 
class Crawler(object):

	def __init__(self, args):
		self.ns = args.ns

	def _getSoup(self, url):
		req = urllib2.Request(
			url = url,
			headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.4 (KHTML, like Gecko) Chrome/22.0.1229.94 Safari/537.4'}
		)
		content = urllib2.urlopen(req).read()
		return BeautifulSoup(content)

	def _isLastPage(self, soup):
		if not soup.find(text=re.compile("End of list.")):
			return False
		else:
			return True

	def _getItem(self, soup):
		itemList = soup.findAll('li')
		for item in itemList:
			print item.find('a').string

	def _getNextPage(self, soup):
		nextUrl = 'http://www.sitedossier.com' + soup.ol.nextSibling.nextSibling.get('href')
		self.soup = self._getSoup(nextUrl)

	def start(self):
		url = 'http://www.sitedossier.com/nameserver/' + self.ns
		self.soup = self._getSoup(url)
		self._getItem(self.soup)
		while not self._isLastPage(self.soup):
			self._getNextPage(self.soup)
			self._getItem(self.soup)

def main():
	parser = argparse.ArgumentParser(description='A crawler for sitedossier.com') 
	parser.add_argument('-ns', type=str, required=True, metavar='NAMESERVER', dest='ns', help='Specify the nameserver')
	args = parser.parse_args()

	crawler = Crawler(args)
	crawler.start()

if __name__ == '__main__':
	main()
