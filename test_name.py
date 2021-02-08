import unittest
import name
class TestName(unittest.TestCase):
    def test_name1(self):
        self.assertEqual(name.name("Joy","Zhang"),"Joy Zhang")
        self.assertEqual(name.name("Vivian","Song"),"Vivian Song")
    def test_name2(self):
        self.assertEqual(name.name("1","3"),"1 3")
        self.assertEqual(name.name("a","b"),"a b")
    def test_name3(self):
        self.assertEqual(name.name("Joe",6),"Error")
        self.assertEqual(name.name(5,6),"Error")
if __name__=="__main__":
    unittest.main(verbosity=2)
