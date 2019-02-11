# Trumptails
by Iris Qu for Code Societies Winter 2019 @ The School For Poetic Computation
Live at: https://trumptails.glitch.me

![alt text](https://cdn.glitch.com/08f22420-9c23-45a9-af2e-0a436a44e9d7%2FScreen%20Shot%202019-02-10%20at%2010.47.36%20PM.png?1549903986394)

## What 
Trumptails is an experiment to generate Trump news with simple machine learning algorithms. 
The generated pieces blend New York Times news articles with grimm's fairytales, to imitate the absurdity of news in Trump era. 

## The titles

- The titles are generated realtime, from a neuron network trained on NYT titles from 2000 - 2019. 

- NYT title source scraped from https://spiderbites.nytimes.com/

- Network trained with textgenrnn (https://github.com/minimaxir/textgenrnn)

## The content

- The news content combines hand selected Trump articles from New York Times, and Grimm's fairytales scraped from https://www.cs.cmu.edu/~spok/grimmtmp/.

- Sentences generated with Markov chain generator: https://github.com/jsvine/markovify

## Webapp

The webapp runs on python 3.6 and Flask.

To install dependencies:
```
pip install Flask textgenrnn markovify
```

To start:
```
python3 server.py
```

## Thanks 

Shout out to the amazing humans at SFPC (https://medium.com/sfpc/meet-the-students-of-code-societies-e539a3da788c),
special thanks to Allison Parrish for her class on automatic writing, Everest Pipkin for her scripts for web scraping and Melanie Hoff / Taeyoon Choi / Nabil Hassein / Ying Quan Tan for making code societies happen. 

## Contact

If you have any questions / comments, email me at iris.xiaoyu.qu@gmail.com