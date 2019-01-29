# title

from flask import Flask
from flask import render_template
app = Flask(__name__)

# print(title)
# print('*********************************************************')
# mix
import json
import markovify
text_a = open("../story/nyt.txt").read()
generator_a = markovify.Text(text_a, state_size=3)
text_b = open("../story/grimm.txt").read()
generator_b = markovify.Text(text_b, state_size=3)
combo = markovify.combine([generator_a, generator_b], [8, 1])

from textgenrnn import textgenrnn
textgen = textgenrnn(config_path='./NYT_2000_2019_config.json', weights_path='./NYT_2000_2019_weights.hdf5', vocab_path='./NYT_2000_2019_vocab.json')
titles = textgen.generate(n=1000, prefix="trump", return_as_list=True, temperature = 1)

from random import randint


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/post')
def post():
    num = randint(1, 1000)
    title = titles[num]
    p1 = generator_a.make_short_sentence(140, tries=50).replace("\n", " ")
    x1 = combo.make_sentence(tries=50).replace("\n", " ")
    x2 = combo.make_sentence(tries=50).replace("\n", " ")
    x3 = combo.make_sentence(tries=50).replace("\n", " ")
    p3 = generator_b.make_short_sentence(100, tries=50).replace("\n", " ")
    p2 = x1 + ' ' + x2 + ' ' + x3
    outputJson = { 'title': title, 'p1': p1, 'p2': p2, 'p3': p3 }
    output = json.dumps(outputJson)
    return output

