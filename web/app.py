# flask web/app.py

# Import the flask module
from flask import Flask
import socket

# Create a Flask constructor. It takes name of the current module as the argument
app = Flask(__name__)

docker_short_id = socket.gethostname()

@app.route('/')
def hello_world():
    return 'Hey, we have Flask in a Docker container with id: ' + docker_short_id


if __name__ == '__main__':
    # call the run method
    app.run(debug=True, host='0.0.0.0')
