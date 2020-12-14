from flask import Flask, render_template, redirect, request

app = Flask(__name__)

FAVORITE_GAMES = []


@app.route('/test')
def test():
    return render_template('test.html')


@app.route('/')
def index():
    return render_template('index.html', favorite_games=FAVORITE_GAMES)


@app.route('/add', methods=['POST'])
def add_game():
    name = request.form['name']
    game = request.form['game']
    FAVORITE_GAMES.append({'name': name, 'game': game})
    return redirect('/')
