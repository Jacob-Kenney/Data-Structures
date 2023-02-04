#Class for node
  
  #function to initialise an instance of node, taking data, next node (default as None), and previous node (default as None) as input
    #set node instance variable, data, to data input
    #set node instance variable, next node, to next node input
    #set instance variable, previous node, to previous node input
   
  #function to set a node's instance variable, next node, taking next node as input
    #set node instance variable, next node, to next node input
  
  #function to set a node's instance variable, previous node, taking previous node as input
    #set node instance variable, previous node, to previous node input

#Class for doubly linked list

  #function to initialise an instance of doubly linked list, taking no input
    #set doubly linked list instance variable, head node, to none
  
  #function to add to the head of this instance of doubly linked list, taking value as input
    #assign a temporary variable (new head) to a node instance with data set to value input
    #if doubly linked list head instance variable is not None
      #set previous node instance variable of doubly linked list head node, to new head
      #set next node instance variable of new head to head node of doubly linked list
    #set the head node of this instance of doubly linked list to new head
    #if doubly linked list tail node instance variable is None
      #set the tail node of this instance of doubly linked list to new head
  
  #function to add to the tail of this instance of doubly linked list, taking value as input
    #assign a temporary variable (new tail) to a node instance with data set to value input
    #if doubly linked list tail node instance variable is not None
      #set next node instance variable of doubly linked list tail node, to new tail
      #set previous node instance variable of new tail to tail node of doubly linked list
    #set the tail node of this instance of doubly linked list to new tail
    #if doubly linked list head node instance variable is None
      #set the head node of this instance of doubly linked list to new tail
  
  #function to remove the head of this instance of doubly linked list, taking no input
    #assign a temporary variable (current head) to the head node of this instance of doubly linked list
    #if doubly linked list head node instance variable is None
      #return None
    #assign a temporary variable (new head) to the next node instance variable of doubly linked list head node instance variable
    #set doubly linked list head node instance variable to new head
    #if new head is not None
      #set previous node instance variable of new head to None
    #if current head is the tail node of this instance of doubly linked list
      #call remove tail function on this instance of doubly linked list
      
  
  #function to remove the tail of this instance of doubly linked list, taking no input
    #assign a temporary variable (current tail) to the tail node of this instance of doubly linked list
    #if doubly linked list tail node instance variable is None
      #return None
    #assign a temporary variable (new tail) to the previous node instance variable of doubly linked list tail node instance variable
    #set doubly linked list tail node instance variable to new tail
    #if new tail is not None
      #set next node instance variable of new tail to None
    #if current tail is the head node of this instance of doubly linked list
      #call remove head function on this instance of doubly linked list
