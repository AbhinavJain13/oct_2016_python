
var list = {
   "head": {
      "value": "first",
      "next": null
   }
}

function addAfter(list, after, newv){
 var runner;
 node={
   'value': newv,
   'next': null
       }
   console.log('check the head: ',list.head);

 if(list.head == null){
   // console.log('list.head is: ',list.head)
   return false;
 }
 else{
    console.log('there is at least one node!');
   runner=list.head;
   console.log('runner ',runner);
   console.log('and the val: ',runner.value)
   while(runner){
     if(runner.value==after){
        console.log("found it!");
       node.next=runner.next;
       runner.next=node;
       return true;
     }
     runner=runner.next;
   }
   return "end of code";
 }
}
addAfter(list,"first","second")
console.log(list);






//
