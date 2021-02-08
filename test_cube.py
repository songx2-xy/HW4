import unittest
import cube
class TestCube(unittest.TestCase):
    def test_cube1(self):
        self.assertEqual(cube.cube(3),27)
        self.assertEqual(cube.cube(2),8)
    def test_cube2(self):
        self.assertEqual(cube.cube(25),15625)
        self.assertEqual(cube.cube(0),0)
    def test_cube3(self):
        self.assertEqual(cube.cube("a"),"Error")
        self.assertEqual(cube.cube("b"),"Error")
if __name__=="__main__":
    unittest.main(verbosity=2)
