from flask import Flask, jsonify, render_template, request, json, redirect, url_for
import random
import data
import wiki
import gpt

app = Flask(__name__) 
output = []
highScore = 0
def get_random():
    return random.randint(0, len(data.wiki) - 1)


#use index.html as loading page and give out directions with a coutndown
#create route for homepage
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start', methods= ['POST', 'GET'])
def start():
    if request.method == 'POST':
        num = get_random()
        while num in output:
            num = get_random()

        output.append(num)
        
        wiki_sport = data.wiki[num]["Sport"]
        wiki_article = data.wiki[num]["Text"]

        gpt_sport = data.gpt[num]["Sport"]
        gpt_aritcle = data.gpt[num["Text"]]
        return render_template('base.html' , wiki_sport = wiki_sport, wiki_article = wiki_article, gpt_sport = gpt_sport, gpt_aritcle= gpt_aritcle)
        
#use game.html to load game with screen
#if correct guess render 'win.html' , update Title, Subsection, Text, rest for 1.5 sec, return render_template  'base.html'
#else render 'lose.html', rest for 1.5 sec, return render_template 'base.html'
#create route for starting game
#app.route('/game', methods = ['POST', 'GET'])

if __name__ == "__main__":
    app.run(debug = True)
