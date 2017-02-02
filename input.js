const fs = require('fs');
fs.readFile('input.txt', function read(err, data) {
  if (err) {
    throw err;
  }
  var words = [];
  fs.readFile('words.txt', function read(err, wordData) {
    if (err) {
      throw err;
    }
    words = wordData.toString().split("\n");
  });
  arrOfAllData = data.toString().split("\n");
  for(var i = 0 ; i < arrOfAllData.length; i++){
    for(var x = 0; x < words.length; x++){
      if(x.isSubstring(arrOfAllData[i])){
        fs.writeFile("beginning.txt", arrOfAllData[i-1]);
        fs.writeFile("middle.txt", arrOfAllData[i]);
        fs.writeFile("end.txt", arrOfAllData[i+1]);
      }
    }
  }
});
