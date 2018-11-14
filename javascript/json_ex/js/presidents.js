function update_demo(obj) {
	var out = "";
	var i;
	for (var key in obj) {
		if (!obj.hasOwnProperty(key)) continue;
		var elem = obj[key];
		var s = JSON.stringify(elem);
		out = out + " :DD: " + s;
	}
	document.getElementById("demo").innerHTML = out;

}

