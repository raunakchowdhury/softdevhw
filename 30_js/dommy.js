// Raunak Chowdhury and Sarar Aseer
// SoftDev1 pd8
// K30 -- Sequential Progression III: Season of the Witch
// 2018-12-20

var storedHeading = document.getElementById("h").innerHTML;
var fib_counter = 1;

var changeHeading = function(e) {
    var h = document.getElementById("h")
    h.innerHTML = e['target']['innerHTML'];
};

var removeItem = function(e) {
  document.getElementById('thelist').removeChild(e['target'])
};

var restoreText = function(e){
  var h = document.getElementById("h")
  h.innerHTML = storedHeading;
};

var lis = document.getElementsByTagName("li");

for(var i=0; i < lis.length; i++) {
    lis[i].addEventListener('mouseover', changeHeading);
    lis[i].addEventListener('mouseout', restoreText);
    lis[i].addEventListener('click', removeItem);
};

var addItem = function(e) {
    var list = document.getElementById('thelist');
    var item = document.createElement("li");
    item.innerHTML = "WORD";
    // add EventListeners for the newly created element
    item.addEventListener('mouseover', changeHeading);
    item.addEventListener('mouseout', restoreText);
    item.addEventListener('click', removeItem);
    list.appendChild( item ); //these are all children!
};

var button = document.getElementById("b");
button.addEventListener('click', addItem);

var fib = function(n) {
    if(n < 2){
        return 1;
    } else {
        return fib(n-1) + fib(n-2);
    }
};

var fib2

var addFib = function(e){
  var fiblist = document.getElementById('fiblist');
  var newfib = document.createElement('li');
  newfib.innerHTML = fib(fib_counter);
  fib_counter++;
  fiblist.appendChild( newfib ); //these are all children!
};

var addFib2 = function(e){
  /*
   * retrieves the current list and adds the last two values.
   * if the length is 1 or 2, add li object
   */
  var fiblist = document.getElementById('fiblist');
  var newfib = document.createElement('li');

  // if the length of the list of lis is 1, add an li object with val 1
  // if length < 3, add li object that is the sum of the last two objects
  // NOTE: one element is taken up by something called text, which is related to ol
  var children = fiblist.childNodes;
  var length = children.length;
  if (length < 3){
    newfib.innerHTML = 1;
  }
  else{
    newfib.innerHTML = parseInt(children[length - 1].innerHTML , 10) + parseInt(children[length - 2].innerHTML, 10);
  }
  console.log(children);
  fiblist.appendChild( newfib );
 };

var fb = document.getElementById("fb");
fb.addEventListener("click", addFib2);
