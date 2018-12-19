//Quaff -- Hui Min Wu, Raunak Chowdhury
//SoftDev1 pd8
//K29 -- Sequential Progression
//2018-12-18

var fibonacci = function(n) {
    if (n == 0) {
        return 0;
    } else if (n <= 2) {
        return 1;
    } else {
        return fibonacci(n-2) + fibonacci(n-1);
    };
};

var gcd = function(a, b) {
    if (a < b) {
        //making sure that the first parameter is larger than the second
        return gcd(b, a);
    } else if (b == 0) {
        return a;
    } else if (a == 0) {
        return 0;
    } else {
        return gcd(b, a % b);
    };
};

var arrayName = ["Hui Min", "Zane", "Johnny", "Raunak"];

var randomStudent = function() {
    //generates a random number and multiplies it by the length so the index is within range
    return arrayName[Math.floor(Math.random() * arrayName.length)];
}

//fibonacci button
var fib = document.getElementById("fib");
fib.addEventListener("click", function() {
    console.log(fibonacci(5))
});

//gcd button
var g = document.getElementById("gcd");
g.addEventListener("click", function() {
    console.log(gcd(120, 75))
});

//random student button
var randS = document.getElementById("ran");
randS.addEventListener("click", function() {
    console.log(randomStudent())
});
