from googlesearch import search
File = open("kites.txt","w+")
for I in range(100,1000):
	File.write(str(I))
	File.write('\n')
	ss = str(I) + ' new cases'
	for url in search(ss, tld='com', lang='es', stop=2):
		if str(I) not in url:
			File.write(url)
			File.write('\n')
	print(I)
File.close()