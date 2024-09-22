from flask import Flask

app=Flask(__name__)

@app.route('/',methods=['GET'])
def  hello():
    return "Hello,it's Simple FLASK API"

@app.route('/ml',methods=['GET'])
def  ML():
    return "Hello, ML"

if __name__ == "__main__":
    app.run(debug=True)