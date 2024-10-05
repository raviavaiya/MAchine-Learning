from flask import Flask, jsonify, request
import numpy as np

app=Flask(__name__)

# @app.route('/<int:number>/')
# def  increment(number):
#     print("API called number",number)
#     return "Increament number is "+str(number+1)


# @app.route('/<string:name>/')
# def  increment(name):
#     print("API called name",name)
#     return "my name is "+str(name)

# details=[
#     {'name':'Ravi','address':'surat'}
# ]

# @app.route('/person', methods=['GET'])
# def get_person():
#     return jsonify(details)

@app.route('/Number',methods=['GET'])
def get_number():
    return jsonify({'number': 10})

if __name__ == "__main__":
    app.run(debug=True)