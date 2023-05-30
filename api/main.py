from flask import Flask,request;
from flask_cors import CORS;
import requests
from dotenv import load_dotenv
import os



load_dotenv(dotenv_path="./.env.local")
# print(os.environ.get('REACT_APP_UNSPLASH_KEY')) 
UNSPLASH_API_URL='https://api.unsplash.com/photos/random/'
REACT_APP_UNSPLASH_KEY=os.environ.get('REACT_APP_UNSPLASH_KEY','')
DEBUG=bool(os.environ.get("DEBUG",True))
print(DEBUG)


if not REACT_APP_UNSPLASH_KEY:
    raise EnvironmentError("Please create .env.local file and insert UNSPLASH_KEY there")

app= Flask(__name__)
app.config['DEBUG'] = DEBUG
CORS(app)
# print(__name__)

@app.route('/test')
def helloWorld():
    return "Hello World!"
# set FLASK_APP=main.py flask run  

@app.route('/new-images')
def new_image():
    headers={
        'Accept-version': 'v1',
        'Authorization': 'Client-ID ' + REACT_APP_UNSPLASH_KEY
    }
    word= request.args.get("query")
    params= {
        "query" : word
    }
    response = requests.get(url=UNSPLASH_API_URL, headers=headers,params=params)
    return response.json()

if __name__ == "__main__" :
    app.run(host="0.0.0.0", port=5050)