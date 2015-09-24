

// create a function that will greet a person,
// and assign the function to the `greet` variable
var greet = function( person, message ) {
  var greeting = 'Hello, ' + person + '!';
  console.log( greeting + ' ' + message );
};

function substitute(){
    var myValue = document.getElementById('myTextBox').value;

    if (myValue.length ==  0) {
        alert('please enter a real value in text box!') ;
        return;
    }
    var myTitle = document.getElementById('title');
    myTitle.innerHTML = myValue;
    alert(typeof myValue)


};


document.write("Hello There!! This is direct write from script")

function justAlert(){
    alert("Howdy!!");

}


justAlert()