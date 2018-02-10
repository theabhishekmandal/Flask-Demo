'''
In this flask demo, we will add one more function which  will return a string representation
of the matched alphabets in the given string

- for this function we have to import the searchforletters function from the vsearch method
- now here we create another function decorator that will associate the web URL with the do_search() method
- then we run the flask object

'''

from flask import Flask

from webAppUsingFlask.vsearch import search4letters

app=Flask(__name__)


@app.route('/')
def hello() -> str:
    return 'Hello world from flask'


@app.route('/search4')
def do_search()-> str:
    return str(search4letters("hello world",'abhishek'))


app.run()
