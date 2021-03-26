#import request
from flask import Flask,request

app = Flask(__name__)
@app.route('/area/<radius>',methods = ['GET'])
def area(radius):
     r = request.json
     area = 3.14* float(r["radius"]) * float(r["radius"])
     return {"Area of circle " : area}
if __name__ == "__main__":
    app.run()
