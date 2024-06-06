from flask import Flask, jsonify, request

app = Flask(__name__)

# endpoint to send greeting
books = [
    {
      "author": "me",
      "id": 1,
      "name": "adam sandler",
      "status": "read"
    }
  ]


@app.route('/greeter/hello', methods=['GET'])
def sayHello():
    return jsonify({'books': books})


if __name__ == '__main__':
    app.run()