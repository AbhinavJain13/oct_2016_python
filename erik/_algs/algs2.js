

// Reverse an array
var aData = ['bob','joe','tom','erik'];
function reverseArray(ary){
   var len = ary.length;
   var temp;
   // start at end, swap towards middle
   for(var i=0;i<length/2;i++){
      ary[i] = ary[length-1-i];
   }
}
reverseArray(aData);


// Reverse the string
// Given a string, return it in reverse order. i.e. 'animal' would return 'lamina'

var data =  'animal';
function reverseString(str){
   var len = str.length;
   var newString = '';
   for(var i=len-1;i>=0;i--){
      newString += str[i];
   }
   return newString;
}
console.log('reverse string: ',reverseString(data));




//
// Parens Valid
// Given a string, return a boolean if the parens are valid. i.e. 'Y(3(p)p(3)r)a' would return true; 'n(a(R)' would return false
//
// Braces Valid
// Given a sequence of parentheses, braces and brackets, determine whether it is valid. i.e. 'W(a{t}s[o(n{ c}o)m]e )h[e{r}e]!' => true. 'D(i{a}l[ t]o)n{e' => false
