# This is basic data mining everyone should know.

# A friend of mine claimed that if you google 'x new cases'(where 'x' is any 
# three-digit number), you'll find an actual headline with that number in the
# search results. I wrote this script to test his claim.

from bs4 import beautifulsoup
from googlesearch import search
import requests
file = open("kites.txt","w+")
for i in range(100,1000):
	file.write(str(i) + '\n')
	ss = str(i) + ' new cases'
	for url in search(ss, tld='com', lang='es', stop=5): # search() will return top 5 urls
		if str(i) not in url:
			file.write(url + '\n')
			# Note that it is possible that the 'x new cases' is missing from the
			# url, but it is there in the webpage. So, use 'requests' to get the
			# get the webpage, and 'beautifulsoup' to parse its text. Then, check
			# if the 'x new cases' is there or not.
	print(i)
file.close()
