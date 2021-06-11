from flask import Flask, render_template, jsonify, request
from flask_restful import Api, Resource

app =Flask(__name__)
api = Api(app)


def checkPostedData(postedData, functionName):
    if functionName == "add" or functionName== "sunstract" or functionName== "multiply":
        if 'x' not in postedData or 'y' not in postedData:
            return 301
        else:
            return 200

class Add(Resource):
    
    def get(self):
        pass
    
    def post(self):
        postData = request.get_json()

        status_code = checkPostedData( postData, "add")
        if status_code != 200:
            resultMap = {
                "Message": "An error Occured",
                "Status Code": status_code
            }
            return resultMap
        
        x = postData["x"]
        y = postData["y"]
        x = int(x)
        y = int(y)
        result = x + y
        resultMap = {
            'Message': result,
            'Status Code' : 200
        }
        return jsonify(resultMap)

    def put(self):
        pass

    def delete(self):
        pass

class Substract(Resource):
    def get(self):
        pass
    
    def post(self):
        postData = request.get_json()

        status_code = checkPostedData( postData, "substract")
        if status_code != 200:
            resultMap = {
                "Message": "An error Occured",
                "Status Code": status_code
            }
            return resultMap
        
        x = postData["x"]
        y = postData["y"]
        x = int(x)
        y = int(y)
        result = x - y
        resultMap = {
            'Message': result,
            'Status Code' : 200
        }
        return jsonify(resultMap)

    def put(self):
        pass

    def delete(self):
        pass

class Multiply(Resource):
    def get(self):
        pass
    
    def post(self):
        postData = request.get_json()

        status_code = checkPostedData( postData, "multiply")
        if status_code != 200:
            resultMap = {
                "Message": "An error Occured",
                "Status Code": status_code
            }
            return resultMap
        
        x = postData["x"]
        y = postData["y"]
        x = int(x)
        y = int(y)
        result = x * y
        resultMap = {
            'Message': result,
            'Status Code' : 200
        }
        return jsonify(resultMap)

    def put(self):
        pass

    def delete(self):
        pass

class Devide(Resource):
    def get(self):
        pass
    
    def post(self):
        postData = request.get_json()

        status_code = checkPostedData( postData, "add")
        if status_code != 200:
            resultMap = {
                "Message": "An error Occured",
                "Status Code": status_code
            }
            return resultMap
        
        x = postData["x"]
        y = postData["y"]
        x = int(x)
        y = int(y)
        result = x / y
        resultMap = {
            'Message': result,
            'Status Code' : 200
        }
        return jsonify(resultMap)

    def put(self):
        pass

    def delete(self):
        pass


api.add_resource(Add, "/add")
api.add_resource(Substract, "/substract")
api.add_resource(Multiply, "/multiply")
api.add_resource(Devide, "/devide")


if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 