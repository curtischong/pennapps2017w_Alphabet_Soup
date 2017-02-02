var request = require('request');
const fs = require('fs');

var beginning = "";
var middle = "";
var end = "";

var count = 0;
fs.readFile('short_story_ids.txt', function read(err, wordData) {
  var urls = wordData.toString().split(",");
  (function loop() {
    console.log(count);
    request(urls[count], function (error, response) {
      var words = JSON.parse(response.body).replaceAll(/<[^>]*>/g, "").replace(/<p>/g, "").replace(/<\/p>/g, "\n").split("\n");
      beginning += words[0];
      for(var m = 0 ; m < words.length; m++){
        var sentences = words[m].split(".");
        if(sentences.length > 2){
          beginning += sentences[0];
          for(var i = 1; i < words.length - 2; i++){
            middle += words[i];
          }
          end += words[words.length -1];
        }
      }
      if(count < 17){
        count++;
        loop();
      }else{
        fs.writeFile("short_story_beginning.txt", beginning);
        fs.writeFile("short_story_middle.txt", middle);
        fs.writeFile("short_story_end.txt", end);
      }
    });
  })();
});
