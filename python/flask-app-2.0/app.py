from flask import Flask, jsonify, request

app = Flask(__name__)

books = [
    {
      "author": "me",
      "id": 1,
      "name": "adam sandler",
      "status": "read"
    }
  ]

# helper function to generate IDs
def generate_id():
    return len(books) + 1

# endpoint to get all books
@app.route('/reading-list/books', methods=['GET'])
def get_books():
    return jsonify({'books': books})

if __name__ == '__main__':
    app.run()