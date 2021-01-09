import unittest

class TestStringMethods(unittest.TestCase):
    def test_split(self):
        self.assertEqual("a-b-c".split("-"), ["a", "b", "c"])
        
    def test_count(self):
        self.assertEqual("beatiuful".count("u"), 2)
        
    # Complete methods below for the challenge
    def test_swapcase(self):
        self.assertEqual("WaTeR".swapcase(), "wAtEr")
      
    def test_index(self):
        self.assertEqual("kazoo".index("z"), 2)

if __name__ == "__main__":
    unittest.main()