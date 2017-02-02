from urllib.request import Request, urlopen
import lxml.html
from bs4 import BeautifulSoup
import re

caps = "([A-Z])"
prefixes = "(Mr|St|Mrs|Ms|Dr)[.]"
suffixes = "(Inc|Ltd|Jr|Sr|Co)"
starters = "(Mr|Mrs|Ms|Dr|He\s|She\s|It\s|They\s|Their\s|Our\s|We\s|But\s|However\s|That\s|This\s|Wherever)"
acronyms = "([A-Z][.][A-Z][.](?:[A-Z][.])?)"
websites = "[.](com|net|org|io|gov)"

def splitIntoSentences(text):
    text = " " + text + "  "
    text = text.replace("\n"," ")
    text = re.sub(prefixes,"\\1<prd>",text)
    text = re.sub(websites,"<prd>\\1",text)
    if "Ph.D" in text: text = text.replace("Ph.D.","Ph<prd>D<prd>")
    text = re.sub("\s" + caps + "[.] "," \\1<prd> ",text)
    text = re.sub(acronyms+" "+starters,"\\1<stop> \\2",text)
    text = re.sub(caps + "[.]" + caps + "[.]" + caps + "[.]","\\1<prd>\\2<prd>\\3<prd>",text)
    text = re.sub(caps + "[.]" + caps + "[.]","\\1<prd>\\2<prd>",text)
    text = re.sub(" "+suffixes+"[.] "+starters," \\1<stop> \\2",text)
    text = re.sub(" "+suffixes+"[.]"," \\1<prd>",text)
    text = re.sub(" " + caps + "[.]"," \\1<prd>",text)
    if "”" in text: text = text.replace(".”","”.")
    if "\"" in text: text = text.replace(".\"","\".")
    if "!" in text: text = text.replace("!\"","\"!")
    if "?" in text: text = text.replace("?\"","\"?")
    text = text.replace(".",".<stop>")
    text = text.replace("?","?<stop>")
    text = text.replace("!","!<stop>")
    text = text.replace("<prd>",".")
    sentences = text.split("<stop>")
    sentences = sentences[:-1]
    sentences = [s.strip() for s in sentences]
    return sentences
for i in range(1,10):
	connection = urlopen('https://www.fictionpress.com/fiction/Romance/?&srt=4&lan=1&r=10&p='+str(i))

	dom =  lxml.html.fromstring(connection.read())

	links = []
	for link in dom.xpath('//a/@href'):
		if link.startswith("/s/") and link[11] == "1" and link[12] == "/":
			links.append("https://www.fictionpress.com" + link)

	beginning = open("beginning.txt", "a")
	middle = open("middle.txt", "a")
	end = open("end.txt", "a")

	for link in links: 
		html = urlopen(links[0]).read()
		soup = BeautifulSoup(html, "lxml")
		story = soup.find("div", {"id":"storytext"})
		story = str(story).replace("</p><p>", "\n")
		story = re.sub('<[^<]+?>', '', story)
		story = re.sub('\"(.+?)\"', '', story)
		story = story.split('\n')
		for paragraph in story: 
			paragraph = splitIntoSentences(paragraph)
			if len(paragraph) > 2: 
				beginning.write(paragraph[0] + " ");
				for i in range(1, len(paragraph) - 1): 
					middle.write(paragraph[i] + " ")
				end.write(paragraph[len(paragraph) - 1] + " ")

	beginning.close()
	middle.close()
	end.close()
