#!/usr/local/bin/python3

from urllib.request import Request, urlopen

#id_list = open("ids.txt").read()[0:-1].split(",")
link = "https://yourstoryclub.com/story-category/short-stories-love/page/2/"
#print(str(counter) + "/" + str(len(link_list)))
#output.write(urlopen(Request(link, headers={'rel': 'bookmark'})).read()
print(urlopen(Request(link, headers={'rel': 'bookmark'})).read())

"""counter = 0
with open("teen-fic.txt", "wb") as output:
	for link in link_list:
		counter += 1
		print(str(counter) + "/" + str(len(link_list)))
		output.write(urlopen(Request(link, headers={'rel': 'bookmark'})).read())"""
