from flask import render_template, redirect
from app import app
from app.models.player import Player
from app.models.game import Game

@app.route('/')
def index():
    return render_template('index.html', title='RPS')

# @app.route('/play')
# def start():
#     return render_template('play.html')

@app.route('/<player_1_choice>/<player_2_choice>')
def play(player_1_choice, player_2_choice):
    player_1 = Player("Player 1", player_1_choice)
    player_2 = Player("Player 2", player_2_choice)
    game = Game()
    result = game.play_game(player_1, player_2)
    # Result is equal to calling the result of function play_game() declared in the Game class.
    print(result)
    return render_template('index.html', title='RPS', player1=player_1, player2=player_2, result=result)
