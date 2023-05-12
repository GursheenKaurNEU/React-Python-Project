from flask import Flask;

app= Flask(__name__)
# print(__name__)
@app.route('/test')
def helloWorld():
    return "Hello World!"
# set FLASK_APP=main.py flask run  

if __name__ == "__main__" :
    app.run(host="0.0.0.0", port=5050)