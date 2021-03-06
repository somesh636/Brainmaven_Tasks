from Task1 import LRU
import unittest  

class TestLRU(unittest.TestCase): 

    def test_LRU_Class(self): 
        """ Test Case: To check for negative value initialization for the LRU class """
        self.assertRaises(ValueError, LRU, -1)

    def test_put_1(self): 
        """ Test Case: To check for put functionality for one value """
        lru = LRU(5)
        lru.put("1", 1)
        lru.put("2", 2)
        lru.put("3", 3)
        lru.put("4", 4)
        lru.put("5", 5)
        self.assertEqual(lru.get("5"), 5, "should be 5")

    def test_put_2(self): 
        """ Test Case: To check for multiple put functionality after LRU maximum size is achieved """
        lru = LRU(5)
        lru.put("1", 1)
        lru.put("2", 2)
        lru.put("3", 3)
        lru.put("4", 4)
        lru.put("5", 5)
        self.assertEqual(lru.get("5"), 5, "should be 5")
        lru.put("6", 6)
        lru.put("7", 7)
        self.assertEqual(lru.get("6"), 6, "should be 6")
        self.assertEqual(lru.get("7"), 7, "should be 7")

    def test_put_3(self): 
        """ Test Case: To check for put functionality for the value which is not the most recent in the size of LRU """
        lru = LRU(5)
        lru.put("1", 1)
        lru.put("2", 2)
        lru.put("3", 3)
        lru.put("4", 4)
        lru.put("5", 5)
        self.assertEqual(lru.get("5"), 5, "should be 5")
        lru.put("6", 6)
        lru.put("7", 7)
        self.assertEqual(lru.get("6"), 6, "should be 6")
        self.assertEqual(lru.get("7"), 7, "should be 7")
        self.assertRaises(KeyError, lru.get, "1")
        
   
    def test_get_1(self): 
        """ Test Case: To check for get functionality for all the values which was put using put function """
        lru = LRU(5)
        lru.put("1", 1)
        lru.put("2", 2)
        lru.put("3", 3)
        lru.put("4", 4)
        lru.put("5", 5)
        self.assertEqual(lru.get("1"), 1, "should be 1")
        self.assertEqual(lru.get("2"), 2, "should be 2")
        self.assertEqual(lru.get("3"), 3, "should be 3")
        self.assertEqual(lru.get("4"), 4, "should be 4")
        self.assertEqual(lru.get("5"), 5, "should be 5")

    def test_get_2(self): 
        """ Test Case: To check for get functionality for a value that doesn't exist in the LRU cache """
        lru = LRU(5)
        lru.put("1", 1)
        lru.put("2", 2)
        lru.put("3", 3)
        lru.put("4", 4)
        lru.put("5", 5)
        self.assertEqual(lru.get("1"), 1, "should be 1")
        self.assertEqual(lru.get("2"), 2, "should be 2")
        self.assertEqual(lru.get("3"), 3, "should be 3")
        self.assertEqual(lru.get("4"), 4, "should be 4")
        self.assertEqual(lru.get("5"), 5, "should be 5")
        self.assertRaises(KeyError, lru.get, "10")

    def test_get_3(self): 
        """ Test Case: To check for get functionality after multiple put """
        lru = LRU(15)
        lru.put("1", 1)
        lru.put("2", 2)
        lru.put("3", 3)
        lru.put("4", 4)
        lru.put("5", 5)
        self.assertEqual(lru.get("1"), 1, "should be 1")
        self.assertEqual(lru.get("2"), 2, "should be 2")
        self.assertEqual(lru.get("3"), 3, "should be 3")
        self.assertEqual(lru.get("4"), 4, "should be 4")
        self.assertEqual(lru.get("5"), 5, "should be 5")
        self.assertRaises(KeyError, lru.get, "10")
        lru.put("6", 6)
        lru.put("7", 7)
        lru.put("8", 8)
        lru.put("9", 9)
        lru.put("10", 10)
        self.assertEqual(lru.get("10"), 10, "should be 10")
        self.assertEqual(lru.get("9"), 9, "should be 10")
        self.assertEqual(lru.get("8"), 8, "should be 10")
        self.assertEqual(lru.get("7"), 7, "should be 10")
        self.assertEqual(lru.get("6"), 6, "should be 10")


    def test_delete_1(self): 
        """ Test Case: To check for delete functionality for different scnearios """
        lru = LRU(5)
        lru.put("1", 1)
        lru.put("2", 2)
        lru.put("3", 3)
        lru.put("4", 4)
        lru.put("5", 5)
        lru.delete("5")
        self.assertRaises(KeyError, lru.get, "5")
        self.assertEqual(lru.get("4"), 4, "should be 4")
        self.assertEqual(lru.get("3"), 3, "should be 3")
        lru.delete("3")
        self.assertRaises(KeyError, lru.get, "3")
        lru.delete("1")
        self.assertRaises(KeyError, lru.get, "1")
        self.assertEqual(lru.get("2"), 2, "should be 2")

    def test_delete_2(self): 
        """ Test Case: To check for delete functionality for one value """
        lru = LRU(15)
        lru.put("1", 1)
        lru.put("2", 2)
        lru.put("3", 3)
        lru.put("4", 4)
        lru.put("5", 5)
        lru.delete("5")
        self.assertRaises(KeyError, lru.get, "5")
        self.assertEqual(lru.get("3"), 3, "should be 3")

    def test_delete_3(self): 
        """ Test Case: To check for multiple delete functionality for one value """
        lru = LRU(1)
        lru.put("1", 1)
        lru.delete("1")
        self.assertRaises(KeyError, lru.get, "1")
        self.assertRaises(KeyError, lru.delete, "1")
        

    def test_size_1(self): 
        """ Test Case: To check for size of LRU with put and get functionality """
        lru = LRU(5)
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
        
        self.assertEqual(lru.get("10"), 10, "should be 10")
        self.assertRaises(KeyError, lru.get, "1")
        self.assertEqual(lru.get("9"), 9, "should be 9")
        self.assertRaises(KeyError, lru.get, "2")
        self.assertEqual(lru.get("8"), 8, "should be 8")
        self.assertRaises(KeyError, lru.get, "3")
        self.assertEqual(lru.get("7"), 7, "should be 7")
        self.assertRaises(KeyError, lru.get, "5")
        self.assertEqual(lru.get("6"), 6, "should be 6")

    def test_size_2(self): 
        """ Test Case: To check for size of LRU with multiple put and get functionality with different size initialization """
        lru = LRU(5)
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
        
        self.assertEqual(lru.get("10"), 10, "should be 10")
        self.assertRaises(KeyError, lru.get, "1")
        self.assertEqual(lru.get("9"), 9, "should be 10")
        self.assertRaises(KeyError, lru.get, "2")
        self.assertEqual(lru.get("8"), 8, "should be 10")
        self.assertRaises(KeyError, lru.get, "3")
        self.assertEqual(lru.get("7"), 7, "should be 10")
        self.assertRaises(KeyError, lru.get, "5")
        self.assertEqual(lru.get("6"), 6, "should be 10")

        lru = LRU(10)
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

        self.assertEqual(lru.get("1"), 1, "should be 1")
        self.assertEqual(lru.get("2"), 2, "should be 2")
        self.assertEqual(lru.get("3"), 3, "should be 3")
        self.assertEqual(lru.get("4"), 4, "should be 4")
        self.assertEqual(lru.get("5"), 5, "should be 5")
        self.assertEqual(lru.get("6"), 6, "should be 6")
        self.assertEqual(lru.get("7"), 7, "should be 7")
        self.assertEqual(lru.get("8"), 8, "should be 8")
        self.assertEqual(lru.get("9"), 9, "should be 9")
        self.assertEqual(lru.get("10"), 10, "should be 10")


    def test_reset_1(self): 
        """ Test Case: To check the reset funcitonality for the LRU algorithm """
        lru = LRU(5)
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
        
        self.assertEqual(lru.get("10"), 10, "should be 10")
        self.assertRaises(KeyError, lru.get, "1")
        self.assertEqual(lru.get("9"), 9, "should be 9")
        self.assertRaises(KeyError, lru.get, "2")
        lru.reset()
        self.assertRaises(KeyError, lru.get, "9")

    def test_reset_2(self): 
        """ Test Case: To check for reset functionality of LRU with put and get functionality """
        lru = LRU(5)
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

        lru.reset()
        self.assertRaises(KeyError, lru.get, "10")
        
    def test_reset_3(self): 
        """ Test Case: To check for reset functionality of LRU put and get functionality after using reset """
        lru = LRU(5)
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

        lru.reset()
        self.assertRaises(KeyError, lru.get, "10")   
        lru.put("1", 1)
        lru.put("2", 2)
        lru.put("3", 3)
        lru.put("4", 4)
        lru.put("5", 5)
        self.assertEqual(lru.get("1"), 1, "should be 1")

if __name__ == '__main__':
    unittest.main()
