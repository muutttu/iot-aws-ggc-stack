# flask web/app.py

# Import the flask module
from flask import Flask

# Create a Flask constructor. It takes name of the current module as the argument
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hey, we have Flask in a Docker container!'


if __name__ == '__main__':
    # call the run method
    app.run(debug=True, host='0.0.0.0')
