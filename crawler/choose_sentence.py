import requests
import json

paragraph = "math is very intersting, it loves to make triangles. it reminds me of squares. it's like a line graph. this is so cool!"
context = "values"
sentences = paragraph.split(".")
def getValue(theContext, theSentences):
    url = "http://api.cortical.io/rest/compare"
    querystring = {"retina_name":"en_associative"}
    #payload = "[\n     { \n        \"term\": \"Pablo Picasso\" \n     },\n     {\n        \"text\": \"Gustav Klimt was born in Baumgarten, near Vienna in Austria-Hungary, the second of seven children\"\n     }\n]"
    payload = "[ {\"term\": \"" + theContext+ "\"},{\"text\": \"" + theSentences + "\"}]"
    headers = {
        'accept': "application/json",
        'origin': "http://api.cortical.io",
        'user-agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.90 Safari/537.36",
        'content-type': "application/json",
        'referer': "http://api.cortical.io/Compare.htm",
        'accept-encoding': "gzip, deflate",
        'accept-language': "en-GB,en-US;q=0.8,en;q=0.6",
        'cookie': "_ga=GA1.2.674882336.1485061533; _gauges_unique_hour=1; _gauges_unique_day=1; _gauges_unique_month=1; _gauges_unique_year=1; _gauges_unique=1",
        'cache-control': "no-cache",
        'postman-token': "58477186-0dbc-1781-560a-25352abe1f7f"
        }
    results = requests.request("POST", url, data=payload, headers=headers, params=querystring)
    return json.loads(results.text).get("cosineSimilarity")

def bestSentence(theContext, allTheSentences):
    max = -0.5
    maxPhrase = ""
    for x in allTheSentences:
      currValue = getValue(theContext,x)
      if currValue is not None:
          if currValue > max:
            maxPhrase = x
            max = currValue
    return maxPhrase
print(bestSentence(context, paragraph.split(".")))
