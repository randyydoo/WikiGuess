from flask import Flask, jsonify, render_template, request, json, redirect, url_for
import random
import data
import wiki
import gpt
import time

app = Flask(__name__) 
output = []
score = 0
highScore = 0

#use index.html as loading page and give out directions with a coutndown
#create route for homepage
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start', methods= ['POST', 'GET'])
def start():
    num = random.randint(0, len(data.wiki) - 1)
    while num in output or "ISBN" in data.wiki[num]["Text"]:
        num = random.randint(0, len(data.wiki) - 1)
        #keep track of used text
    output.append(num)
    if request.method == 'POST':
        wiki_sport = data.wiki[num]["Sport"]
        wiki_article = data.wiki[num]["Text"]

        gpt_sport = data.gpt[num]["Sport"]
        gpt_article = data.gpt[num]["Text"]
        return render_template('base.html' , score = score, wiki_sport = wiki_sport, wiki_article = wiki_article, gpt_sport = gpt_sport, gpt_article = gpt_article)
    #handle false https request
    else:
        return redirect("/")
       
#use game.html to load game with screen
#if correct guess render 'win.html' , update Title, Subsection, Text, rest for 1.5 sec, return render_template  'base.html'
#else render 'lose.html', rest for 1.5 sec, return render_template 'base.html'
#create route for starting game
#app.route('/game', methods = ['POST', 'GET'])

if __name__ == "__main__":
    app.run(debug = True)
