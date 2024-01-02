from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World"

@app.route("/api", methods=['GET'])
def returnascii():
    d = {}
    inputChar = str(request.args['query'])
    answer = str(ord(inputChar))
    d['output'] = answer
    return d

# if __name__ == "__main__":
#     app.run()
