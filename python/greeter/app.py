from flask import Flask, jsonify, request

app = Flask(__name__)

# endpoint to send greeting

@app.route('/greeter/hello', methods=['GET'])
def sayHello(myname):
    if myname:
        return f"Hello {myname}"
    else:
        return "Hello stranger!"


if __name__ == '__main__':
    app.run()