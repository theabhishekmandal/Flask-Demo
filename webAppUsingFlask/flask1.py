'''
      here we import the flask web framework which we will run on out local host
      flask is the module name and Flask is the name of the class.
      -so first we create a Flask object by passing the name of the current module.
      -then we create a function decorator which lets us to associate a URL web path with existing
      python function.
      -then we define the function named hello which will display a string message on the screen
'''

from flask import Flask

app=Flask(__name__)

@app.route('/')
def hello() -> str:
    return 'Hello world from flask'


app.run()
