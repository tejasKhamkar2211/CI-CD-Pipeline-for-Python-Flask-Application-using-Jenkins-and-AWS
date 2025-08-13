import unittest
from app import app, check_winner

class TicTacToeTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    # ---------------------------
    # Test HTML Routes
    # ---------------------------
    def test_home_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Play with Computer', response.data)

    def test_play_computer_page(self):
        response = self.app.get('/play/computer')
        self.assertEqual(response.status_code, 200)

    def test_play_friends_page(self):
        response = self.app.get('/play/friends')
        self.assertEqual(response.status_code, 200)

    # ---------------------------
    # Test check_winner logic
    # ---------------------------
    def test_check_winner_x_wins(self):
        board = ["X", "X", "X", "", "", "", "", "", ""]
        self.assertEqual(check_winner(board), "X")

    def test_check_winner_o_wins(self):
        board = ["O", "", "", "O", "", "", "O", "", ""]
        self.assertEqual(check_winner(board), "O")

    def test_check_draw(self):
        board = ["X", "O", "X", "X", "O", "O", "O", "X", "X"]
        self.assertEqual(check_winner(board), "Draw")

    def test_check_none(self):
        board = ["X", "O", "", "", "", "", "", "", ""]
        self.assertIsNone(check_winner(board))

    # ---------------------------
    # Test API Routes
    # ---------------------------
    def test_computer_move_api(self):
        board = ["X", "", "", "", "", "", "", "", ""]
        response = self.app.post('/api/computer_move', json={'board': board})
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn("board", data)
        self.assertIn("winner", data)

    def test_friends_move_api(self):
        board = ["X", "O", "X", "", "", "", "", "", ""]
        response = self.app.post('/api/friends_move', json={'board': board})
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn("winner", data)


if __name__ == '__main__':
    unittest.main()

