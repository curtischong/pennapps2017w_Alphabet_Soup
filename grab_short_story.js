var request = require('request');
const fs = require('fs');
var count = 1;
var links = "";
(function loop() {
  if(count < 188){
    console.log(count);
    request('http://yourstoryclub.com/story-category/short-stories-love/page/'+count, function (error, response) {
      data = response.body.split("\n");
      for(var i = 0 ; i < data.length; i++){
        if(data[i].includes('rel="bookmark"')){
          links += (data[i].split('<a href="')[1].split('" rel=')[0]) + ",";
        }
      }
      count++;
      loop();
    });
  }else{
    fs.writeFile("short_story_ids.txt", links, function(err) {
      if(err) {
        console.log(err);
      }
    });
  }
}());
