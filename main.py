import pymongo
from flask import Flask, render_template, redirect

app = Flask(__name__)

conn = 'mongodb://localhost:27017'

client = pymongo.MongoClient(conn)

db = client.mlbDB

@app.route('/')
def index():
    top_hitter = db.top_hitters.find_one()
    #print(mars)
    if top_hitter is None: #on first run, there won't be a database nor results, so initial force redirect to scrape.
        print('error!')
    else:
        return render_template('index.html', player_vars = top_hitter)

if __name__ == "__main__":
    app.run(debug=True)