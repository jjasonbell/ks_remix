function weightedRand(ycarray) {
  var i; 
  var sum = 0; 
  r = Math.random();
	var arrayLength = ycarray.length;
	for (var i = 0; i < arrayLength; i++) {
    json_i = ycarray[i];
    sum += json_i['Weight'];
    if (r <= sum) return json_i;
  }
}

