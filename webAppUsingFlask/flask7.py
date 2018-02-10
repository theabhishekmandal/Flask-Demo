'''
- In the previous flask demo we were getting the input from the user and
  then we were displaying the result to the browser

- here we will also show the result but through the html document results.html

- To do this we modify the do_search method

- Also here we will redirect the @app.route('/') to our main page and we will remove the hello method from
  this program
'''

from flask import Flask, render_template,request

from webAppUsingFlask.vsearch import search4letters

app=Flask(__name__)


# this allows the POST to get matched with the POST associated with the entry.html
# this method won't work if POST is not given
# here we take input from the user using request
# we also render the results.html file to the browser

@app.route('/search4',methods=['POST'])
def do_search()-> 'html':
    phrase=request.form['phrase']
    letters=request.form['letters']
    title="Here are your results "
    results=str(search4letters(phrase,letters))
    return render_template('results.html',the_title=title,the_results=results,the_phrase=phrase,the_letters=letters)


# here rendertemplate should contain the html page which it will going to render
@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html',the_title='Welcome to search for letters on the web')


app.run(debug=True)
