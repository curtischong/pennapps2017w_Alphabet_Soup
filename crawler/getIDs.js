var request = require('request');
const fs = require('fs');
var theNextUrl = 'https://www.wattpad.com/api/v3/stories?category=1&fields=stories%28id%2Ctitle%2CvoteCount%2CreadCount%2CcommentCount%2Cdescription%2Ccover%2Ccompleted%2Crating%2Crankings%2Cmature%2Curl%2Ctags%2CnumParts%2CfirstPartId%2CmodifyDate%2Ccategories%2Cuser%28name%2Cavatar%29%29%2Ctotal%2CnextUrl%2Ctags&filter=hot&limit=18&offset=36';
var count = 0;
var theStories ="";
(function loop() {
  request(theNextUrl, function (error, response) {
    var stories = JSON.parse(response.body).stories;
    for(var x = 0; x < stories.length; x++){
      theStories += stories[x].firstPartId + ",";
    }
    theNextUrl = JSON.parse(response.body).nextUrl;
    count++;
    console.log(count);
    if(count < 82){
      loop();
    }else{
      fs.writeFile("ids.txt", theStories, function(err) {
        if(err) {
          return console.log(err);
        }
        console.log("The file was saved!");
      });
    }
  });
}());
