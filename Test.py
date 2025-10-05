import unittest
from GameOfLife import Cell, GridClass

class TestCalculations(unittest.TestCase):

    def test_calculations(self):
        Cell = Cell()
        self.assertEqual(Cell.CheckNeighbours([
 [0, 1, 0],
 [1, 1, 0],
 [0, 0, 1]
], True, 1), 1, 'The check Neighhour Function is wrong.')

   
if __name__ == '__main__':
    unittest.main()