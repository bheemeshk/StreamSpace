var i = 0; 

do {
	if (i == 2){ 
		continue; 
	}
	document.write( i + "<p>I will not drive in wrong zone!</p>" );
	i = i + 1;
} while (i < 10) 