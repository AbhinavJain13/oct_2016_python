function find(list,val){
   var current = list.head;
   while(current){
      if(current.val == val){
         return true;
      }
      current = current.next;
   }
   return false;
}
