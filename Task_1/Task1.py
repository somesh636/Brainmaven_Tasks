from collections import OrderedDict

class LRU(OrderedDict):
    """ This class is an implementation of Least Recently Used (LRU) using OrderedDict 

	Parameters: 
	-----------
	max_size: int(default: 10)
	          Maximum size requierd for the implementation
		
	
	Attributes:
	-----------
	None 
    """ 

    def __init__(self, max_size=5): 
        """ Initialization Fucntion for the clas  """
        if max_size<0: 
            raise ValueError 

        self.max_size = max_size 
        super().__init__()

    def put(self, key, value):
        """ Inserts a value to its key 
        Parameters: 
        -----------
        key: key for the value             
        
        value: value for the associated key 

        Attributes:
        -----------
        None 
        """
        try: 
            value = self.pop(key)
        
        except KeyError: 
            if len(self) >= self.max_size: 
                self.popitem(last=False)
        
        self[key] = value 
            

    def get(self, key): 
        """ Returns the value associated with the key 
        Parameters: 
        -----------
        key: key for the value   
        
        Attributes:
        -----------
        value: value for the associated key 
        """
        try: 
            value = self.pop(key) 
            self[key] = value 
            return value 

        except KeyError: 
            raise KeyError

    def delete(self, key):
        """ Deletes a the value for the given key 
        Parameters: 
        -----------
        key: key for the value   
        
        Attributes:
        -----------
        value: value for the associated key 
        """
        try: 
            self.pop(key)
        
        except KeyError: 
            raise KeyError

if __name__ == "__main__": 

    # Exploratory Testing 
    lru = LRU(5)
    lru.put("5", "sg")
    lru.put("6", "pg")
    lru.put("7", "s")
    lru.put("8", "p")
    lru.put("9", "so")
    lru.put("10", "pr")
    lru.put("11", "som")
    lru.put("12", "pri")
    lru.delete("10")
    value = lru.get("12")
    print(value) 
    value1 = lru.get("7")
    print(value1)  
    value2 = lru.get("100")
    print(value2) 
    value3 = lru.get("5")
    print(value3) 
    value4 = lru.get("12")
    print(value4)
    
    






