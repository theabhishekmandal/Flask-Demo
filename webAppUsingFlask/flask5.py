'''
  Everything is same from the previous module but here we turn on the debugging mode
  the benefit of doing so is that whenever their are changes in the webapp then Flasks automatically
  restarts it. Thereby increasing our efficiency by not stopping the running code, while we make changes in the code

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


app.run(debug=True)
