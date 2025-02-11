import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_rows = 10
        num_cols = 12
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10,)
        self.assertEqual(len(m1.cells), num_cols,)
        self.assertEqual(len(m1.cells[0]), num_rows,)

    def test_maze_extreme_params(self):
        num_rows = 0
        num_cols = 50
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10,)
        self.assertEqual((m1.num_cols * m1.cell_size_x), 500)
    
    def test_walls_broken(self):
        num_rows = 10
        num_cols = 12
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10,)
        m1._create_cells()
        m1._break_entrance_and_exit()
        self.assertEqual(m1.cells[0][0].walls["top_wall"], False)
        self.assertEqual(m1.cells[num_cols][num_rows].walls["bottom_wall"], False)


if __name__ == "__main__":
    unittest.main()