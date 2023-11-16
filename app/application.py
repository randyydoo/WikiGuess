from flask import Flask, jsonify, render_template
import random
import data

application = Flask(__name__) 
output = []

@application.route('/get_text')
def wiki_text():
    json_obj = {}
    num = random.randint(0, len(data.wiki) - 1)
    while num in output:
        num = random.randint(0, len(data.wiki) - 1)
    json_obj["Wiki"] = data.wiki[num]["Text"]
    json_obj["Gpt"] = data.gpt[num]["Text"]
    json_obj["Random"] = random.randint(0,1)
    return jsonify(json_obj)

#create route for homepage
@application.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    application.run()
