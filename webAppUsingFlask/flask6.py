'''
In the previous flask program demo, we could see that the do_search methods have the arguments hard coded inside the function.
that's why we cannot change the values accordingly .

- to get the input from the user everytime when you run the webapp, we will use the Flask request method,
  to get the values from the user

- Flask request object contains a dictionary attribute called form which provides easy access to HTML
  form's data posted from the browser

- A form is like python dictionary which supports square bracket notation
'''

from flask import Flask, render_template,request

from webAppUsingFlask.vsearch import search4letters

app=Flask(__name__)


@app.route('/')
def hello() -> str:
    return 'Hello world from flask'


# this allows the POST to get matched with the POST associated with the entry.html
# this method won't work if POST is not given
# here we take input from the user using request
@app.route('/search4',methods=['POST'])
def do_search()-> str:
    phrase=request.form['phrase']
    letters=request.form['letters']
    return str(search4letters(phrase,letters))


# here rendertemplate should contain the html page which it will going to render

@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html',the_title='Welcome to search for letters on the web')



app.run(debug=True)
