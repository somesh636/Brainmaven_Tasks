from collections import OrderedDict

class LRU(OrderedDict):
    """ This class is an implementation of Least Recently Used (LRU) using OrderedDict 

	Parameters: 
	-----------
	max_size: int(default: 5)
	          Maximum size requierd for the implementation
		
	
	Attributes:
	-----------
	None 
    """ 

    def __init__(self, max_size=5): 
        """ Initialization Fucntion for the class  """
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

    def reset(self):
        """ Deletes all the key values from the LRU 
        Parameters: 
        -----------
        None   
        
        Attributes:
        -----------
        None 
        """
        self.clear()


if __name__ == "__main__": 

    # Exploratory Testing 
    lru = LRU(15)
    lru.put("11", "sg")
    lru.put("12", "pg")
    lru.put("13", "s")
    lru.put("14", "p")
    lru.put("15", "so")
    lru.put("16", "pr")
    lru.put("17", "som")
    lru.put("18", "pri")
    lru.put("1", 1)
    lru.put("2", 2)
    lru.put("3", 3)
    lru.put("4", 4)
    lru.put("5", 5)
    lru.put("6", 6)
    lru.put("7", 7)
    lru.put("8", 8)
    lru.put("9", 9)
    lru.put("10", 10)

    value_1 = lru.get("1")
    value_2 = lru.get("2")
    value_3 = lru.get("3")
    value_4 = lru.get("4")
    value_5 = lru.get("5")
    value_6 = lru.get("6")
    value_7 = lru.get("7")
    value_8 = lru.get("8")
    value_9 = lru.get("9")
    value_10 = lru.get("10")
    
    print(value_1)
    print(value_2)
    print(value_3)
    print(value_4)
    print(value_5)
    print(value_6)
    print(value_7) 
    print(value_8)
    print(value_9)
    print(value_10)



    
    






