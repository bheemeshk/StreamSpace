var sauce = -1;
var crust = prompt("what kind of crust do you want? thin or regular?"); 
document.write('You are accessing this page from ' + location.hostname + ' ' + name  );


if ((crust == 'thin') || (crust == 'regular')){
	var cheese = prompt("Choose your cheese."); 
	switch(cheese){
	
		case 'mozarella':
		case 'feta':
		case 'parmesan':
			sauce = 'tomato';
		break;
		case 'cheddar':
			sause = 'white';
		break;
		
		default:
			alert("Sorry we do not have that kind of cheese") ; 
		break;
	}
	
	if (sauce != -1) {
		alert('You ordered a pizza with ' + crust + ' crust ' + cheese + ' cheese and ' + sauce + ' sauce')
	}
} else{
	alert("Sorry we do not server that kind of crust") ;
	
}
