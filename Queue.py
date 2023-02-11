#Class for Node

  #function to initialise an instance of node, taking data as input
    #set node instance variable, data, to data input
    #set node instance variable, next node, to None
    
  #function to set a node's instance variable, next node, taking next node as an input
    #set node instance variable, next node, to next node input
    
#Class for Queue

  #function to initialise an instance of queue, taking no input
    #set queue instance variable, head, to None
    #set queue instance variable, tail, to None
    
  #function to enqueue (add a node to the queue's tail), taking value as input
    #assign a temporary variable (new tail) to a Node instance with data set to value input
    #if queue head instance variable is None
      #set queue head instance variable to new tail
      #set queue tail instance variable to new tail
    #else
      #set next node instance variable of the tail of this queue to new tail
      #set the tail node of this instance of queue to new tail
  
  #function to peek (view head without modifying the state of the queue), taking no input
    #if head of this instance of queue is None
      #return head 
    #else
      #return head instance variable, data
  
  #function to dequeue (remove and return the queue's head), taking no input
