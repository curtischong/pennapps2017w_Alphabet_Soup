var request = require('request');

url = "https://api.meaningcloud.com/topics-2.0?key=4e9d9d2ab61341074dd513e4422aa47e&of=json&lang=en&ilang=en&txt=" + inputData

request(url, function (error, response, body) {
  if (!error && response.statusCode == 200) {
    console.log(body) // Show the HTML for the Google homepage. 
  }
})