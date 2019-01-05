function weightedRand(ksarray) {
  var i; 
  var sum = 0; 
  r = Math.random();
	var arrayLength = ksarray.length;
	for (var i = 0; i < arrayLength; i++) {
    json_i = ksarray[i];
    sum += json_i['Weight'];
    if (r <= sum) return json_i;
  }
}

