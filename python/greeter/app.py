from flask import Flask, jsonify, request

app = Flask(__name__)

# endpoint to send greeting

@app.route('/hello', methods=['GET'])
def sayHello():
    return "Hello user"


if __name__ == '__main__':
    app.run()