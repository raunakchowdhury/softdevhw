// Raunak Chowdhury and Sarar Aseer
// SoftDev1 pd8
// K28 -- Sequential Progression
// 2018-12-18

var fib=function fibonacci(n){
  if (n == 0){
    return 0;
  }
  else if (n == 1 || n == 2){
    return 1;
  }
  else{
    return fibonacci(n-1) + fibonacci(n-2);
  };
}

var gcd = function greatest_common_denominator(a,b){
  if (b > a){
    var c = a;
    a = b;
    b = c;
  }
  var rem = a % b;
  if(rem == 0){
    return b;
  }
  return greatest_common_denominator(b,rem);
}

students = ['Sarar', 'Why', 'You', 'Do', 'Dis'];

var rs = function randomStudent(list){
  var student = Math.floor(Math.random() * students.length);
  return list[student];
}
