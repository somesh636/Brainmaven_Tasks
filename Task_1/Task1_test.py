from Task1 import LRU
import unittest  

class TestLRU(unittest.TestCase): 

    def test_LRU_Class(self): 
        self.assertRaises(ValueError, LRU, -1)

    def test_put(self): 
        lru = LRU(5)
        lru.put("1", 1)
        lru.put("2", 2)
        lru.put("3", 3)
        lru.put("4", 4)
        lru.put("5", 5)
        self.assertEqual(lru.get("5"), 5, "should be 5")
    
    def test_get(self): 
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

    def test_delete(self): 
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

    def test_size(self): 
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

        

if __name__ == '__main__':
    unittest.main()