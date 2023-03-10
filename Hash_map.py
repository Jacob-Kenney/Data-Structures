#It should be noted that functionality of hash maps are provided as default in python through the library data type.

#Class for Hash map
  
  #function to initialise an instance of hash map, taking size as input
    #set hash map instance variable, size, to size input
    #set hash map instance variable, array, to an array initialised to none element, size times
    
  #function for the hashing function (which returns the index that each key is stored at in an array), taking key as input
    #assign a temporary variable (key bytes) to a list of bytes formed from key
    #return the sum of key bytes (the hash code)

  #function for a compressor (return an array index from the hash code), taking hash code as input
    #return hash code modulus the length of the array instance variable of this hash map
