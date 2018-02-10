'''
 In this flask demo we will create the entry page of our html through flask

 Flask comes with a function called render_template which, when provided with the name of a
template and any required arguments, returns a string of HTML when invoked. To use
render_template , add its name to the list of imports from the flask module (at the top of your
code), then invoke the function as needed.

  render_template contains arguments such as one is the html page, the other arguments can be
  the default arguments of the html page

- for this we will define a method which will return a html document which we have created
- But after entering the values in the html document we will find that it will show some error
  error no.405
- The 405 status code indicates that the client (your browser) sent a request using a HTTP method
  which this server doesn’t allow
'''

from flask import Flask, render_template

from webAppUsingFlask.vsearch import search4letters

app=Flask("hello world")


@app.route('/')
def hello() -> str:
    return 'Hello world from flask'


@app.route('/search4')
def do_search()-> str:
    return str(search4letters("hello world",'abhishek'))


# here rendertemplate should contain the html page which it will going to render


@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html',the_title='Welcome to search for letters on the web')


app.run()
