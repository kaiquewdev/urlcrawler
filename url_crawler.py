#!/usr/bin/python
#-*-coding:utf-8 -*-

#Url tools, work with a url for read, and indentifier.
class urltools(object):
	def __init__(self, url):
		self.url = url
	def urlread(self):
		'''
		>>> urltools('http://www.google.com').urlread()
		True
		>>> urltools('http://salask.ur').urlread()
		False
		'''
		import urllib2
		url = self.url
		
		if url:
			path = urllib2.urlopen(url)
			scrap = path.read()
			if path:
				if scrap:
					return True
				else:
					return False
			else:
				return False
	
#File tools, work with a file for read, and indentifier.
class filetools(object):
	def fileread(self, path=''):
		pass

class crawler(object):
	def url(self):
		pass

def _test():
	import doctest
	doctest.testmod()

if __name__ == '__main__':
	_test();
