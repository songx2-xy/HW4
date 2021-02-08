import unittest
import average
class TestAverage(unittest.TestCase):
    def test_average1(self):
        self.assertEqual(average.average([2]),2)
        self.assertEqual(average.average([3,6,9]),6)
    def test_average2(self):
        self.assertEqual(average.average([1,1,1,1,1,1]),1)
        self.assertEqual(average.average([0,1,2,3,4,5]),2.5)
    def test_average3(self):
        self.assertEqual(average.average([ ]),"Error")
        self.assertEqual(average.average(["e","b","a"]),"Error")
if __name__=="__main__":
    unittest.main()