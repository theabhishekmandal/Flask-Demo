'''
In this program we will be removing the error that generated in the previous flask demo

- In this we will try to use the  POST method to avoid the error no 405
- here we associate the method='POST' which matches with the POST associated with the entry.html document
- due to this do_search method will get called

'''

from flask import Flask, render_template

from webAppUsingFlask.vsearch import search4letters

app=Flask(__name__)


@app.route('/')
def hello() -> str:
    return 'Hello world from flask'


# this allows the POST to get matched with the POST associated with the entry.html
# this method won't work if POST is not given
@app.route('/search4',methods=['POST'])
def do_search()-> str:
    return str(search4letters("hello world",'abhishek'))


# here rendertemplate should contain the html page which it will going to render


@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html',the_title='Welcome to search for letters on the web')


app.run()
