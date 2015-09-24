var i ; 
document.write("HELLO")
var tbl = ''; 
tbl = '<table>'; 
for(i = 1; i <=20; i++ ) { 
	tbl=tbl+'<tr>';
		for(j = 1; j <= 10; j++) {
			tbl = tbl + '<tr><td>';
			tbl = tbl + i; 
			tbl = tbl + '</td>';
			
			tbl = tbl + '<td>';
			tbl = tbl + ('X '+ j +' = '); 
			tbl = tbl + '</td>';
			
			tbl = tbl + '<td>';
			tbl = tbl + (i*j); 
			tbl = tbl + '</td></tr>';
			}
	tbl=tbl+'</tr>';
	}
tbl = tbl + '</table>';
document.write(tbl);