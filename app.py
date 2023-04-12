from flask import Flask, jsonify, render_template, request, json
from jinja2 import Base, Win, Lose, Index
import random
import data
import wiki
import gpt

app = Flask(__name__) 
output = []
highScore = 0
def get_random():
    return random.randint(0, len(data.wiki) - 1)

def is_used(num):
    if num in output:
        return get_random()

#use index.html as loading page and give out directions with a coutndown
#create route for homepage
app.route('/')
def index():
    return render_template('index.html')

#use game.html to load game with screen
#if correct guess render 'win.html' , update Title, Subsection, Text, rest for 1.5 sec, return render_template  'base.html'
#else render 'lose.html', rest for 1.5 sec, return render_template 'base.html'
#create route for starting game
app.route('/game', methods = ['POST', 'GET'])

if __name__ == "__main__":
    app.run(debug = True)
