

// 1. Remove Blanks:
//
// Create a function that, given a string, returns all of the string's contents, but without blanks.
//
// 'Pl ayTha tF unkyM usi c ' would return 'PlayThatFunkyMusic'
//
// 2. Get Digits:
//
// Create a function that given a string, returns the integer made from this string's digits.
//
// "0s1z3y5w7h9a2t4?6!8?0" would return "01357924680"
//
// 3. Remove Shorter Strings
//
// Given a string array and value(length), remove any strings shorter than the length from the array
//
// ["Today", "is", "Monday", "the", "first", "day", "of", "the", "week"] with a length of 4, would return ["Today", "Monday", "first", "week"]

// 1
var data = "Pl ayTha tF unkyM usi c ";

function removeSpaces(str){
   var len = str.length;
   var i;
   var newString = '';
   for(i=0;i<len;i++){
      if(str[i]!=" "){
         newString = newString + str[i];
      }
   }
   return newString;
}
// console.log(removeSpaces(data));

// 2

var data = "0s1z3y5w7h9a2t4?6!8?0";

function stringToDigitString(data){
   var len = data.length;
   var newString = '';
   for(i=0;i<len;i++){
      if(data[i]>= "0" && data[i]<="9"){
         newString =  newString + data[i];
         // console.log(typeof(data[i])); // they are all string
      }
   }
   return newString;
}
//console.log(stringToDigitString(data));


//3

var data = ["Today", "is", "Monday", "the", "first", "day", "of", "the", "week"];

var check = 4;
function checkLength(ary,check){
   var len = ary.length;
   var newAry = [];
   for(i=0;i<len;i++){
      if(ary[i].length >= check){
         newAry.push(ary[i]);
      }
   }
   return newAry;
}
console.log(checkLength(data,check));










// end
