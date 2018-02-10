
'''
 In this implementation we will read the contents of the file using the readlines() method which reads all the lines
 and returns a list of it.

 Then we will join the list using the join method  See line number 40 and 41
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
        contents=hel.readlines()      # this returns the list of all the lines in the file
    return escape(''.join(contents))  # this combines the list to form a string


if __name__ == '__main__':
    app.run(debug=True)