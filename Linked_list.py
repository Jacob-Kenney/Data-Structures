#Class for node
Class Node:
  
  #function to initialise an instance of node, taking data and next node (default as None) as input
    #set node instance variable, data, to data input
    #set node instance variable, next node, to next node input
    
  #function to set an instance node's next node instance variable, taking next node as an input
    #set node instance variable, next node, to next node input
    
#Class for linked list
  #function to initialise an instance of linked list, taking head node (default as None) as input
    #set linked list instance variable, head, to head node input
    
  #function to add node to the head of an instance of linked list, taking value as input
    #if linked list, head instance variable is None
      #set linked list, head instance variable to a Node instance with data set to value input
    #else
      #assign a temporary variable (new head) to a Node instance with data set to value input
      #set new head next node instance variable to the head node of this instance of linked list
      #set the head node of this instance of linked list to new head
    #return success, node added
    
  #function to remove a node from linked list, taking value as input
    #assign a temporary variable (current) to the head node of this instance of linked list
    #if current's data instance variable is value
      #set the head node of this instance of linked list to the next node instance variable of current
    #while current's next node instance variable is not None
      #if current's next node instance variable value is input value
        #assign a temporary variable (target) to the next node instance variable of current
        #set current's next node instance variable to target's next node instance variable
      #set current to current's next node instance variable
    #return Error, node not present
    
  #function to return linked list as list
    #initialise a temporary variable (result) to list
    #assign a temporary variable (current) to the head node of this instance of linked list
    #while current is not None
      #append current's data instance variable to result
      #assign result to result's next node instance variable
    #return result
