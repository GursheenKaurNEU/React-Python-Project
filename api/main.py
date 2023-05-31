from flask import Flask,request,jsonify;
from flask_cors import CORS;
import requests
from dotenv import load_dotenv
import os
# from mongo_client import insert_test_document
from mongo_client  import mongoClient



gallery = mongoClient.gallery
images_collection = gallery.images

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



@app.route('/images',methods=["GET","POST"])
def images():
    if request.method == 'GET':
        # read images from the db
        images =images_collection.find({})
        return jsonify([img for img in images])
    if request.method == 'POST':
        # save image in the db 
        image = request.get_json();
        image["_id"] = image.get("id")
        result = images_collection.insert_one(image)
        insertedId= result.inserted_id
        return {"inserted_id":insertedId}
        

if __name__ == "__main__" :
    app.run(host="0.0.0.0", port=5050)