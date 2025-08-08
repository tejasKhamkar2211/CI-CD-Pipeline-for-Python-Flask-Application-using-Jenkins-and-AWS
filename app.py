from flask import Flask, render_template, request, redirect, url_for, jsonify
import random

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/play/computer')
def play_computer():
    return render_template('play_computer.html')

@app.route('/play/friends')
def play_friends():
    return render_template('play_friends.html')

def check_winner(board):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    for combo in winning_combinations:
        a, b, c = combo
        if board[a] and board[a] == board[b] == board[c]:
            return board[a]
    if all(cell != "" for cell in board):
        return "Draw"
    return None

@app.route('/api/computer_move', methods=['POST'])
def computer_move():
    data = request.json
    board = data['board']
    available = [i for i in range(9) if board[i] == ""]
    if available:
        move = random.choice(available)
        board[move] = "O"
    winner = check_winner(board)
    return jsonify({'board': board, 'winner': winner})

@app.route('/api/friends_move', methods=['POST'])
def friends_move():
    data = request.json
    board = data['board']
    winner = check_winner(board)
    return jsonify({'winner': winner})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

