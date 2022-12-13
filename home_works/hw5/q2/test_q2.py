import q2
from algo import DFS,BFS
import unittest

graph_to_tests = [[0, 1, 1, 0, 0, 0],[1, 0, 1, 1, 0, 0],[1, 0, 0, 1, 0, 0],[0, 0, 1, 0, 0, 0],[0, 0, 0, 0, 0, 1],[0, 0, 0, 0, 1, 0],]
# x = q2.serch_in_graph(BFS,graph_to_tests,0)
# print(x)


class TestQ2(unittest.TestCase):
    def test_serch_in_graph(self):
        self.assertEqual(q2.serch_in_graph(BFS,graph_to_tests,0), [0,1,2,3])


if __name__ == "__main__":
    unittest.main()