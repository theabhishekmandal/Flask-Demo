
'''
- In the previous program we use the dir() method on the flask_request object to know what does this object contains.
  what types of methods does it contains. But we got so many unnecessary stuff.

  In this program we will basically use three attributes
    req.form - the data posted from webapp's html form.
    req.remote_addr - the ip address web browser is running on.
    req.user_agent.string - the identify of the browser posting data.
'''

from flask import Flask, render_template, request ,escape

from webAppUsingFlask.vsearch import search4letters

app= Flask(__name__)


@app.route('/')
@app.route('/entry')
def entry() -> 'html':
    return render_template('entry.html', the_title='Welcome to search for letters on the web')


@app.route('/search4', methods=['POST'])
def do_search() -> str:
    phrase= request.form['phrase']
    letters= request.form['letters']
    title= "Here are your results"
    result=str ( search4letters(phrase, letters))
    log_request(request, result)
    return render_template('results.html', the_title=title, the_phrase=phrase, the_results=result, the_letters=letters)


def log_request(req:' flask_request',res: str) -> None:
    with open('vsearch.log','a') as log:
        print(req.form,req.user_agent.string,req.remote_addr,res,file=log,sep='|')


@app.route('/viewlog')
def showlog() -> str:
    with open('vsearch.log') as hel:
        contents=hel.read()
    return escape(contents)


if __name__ == '__main__':
    app.run(debug=True)