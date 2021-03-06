
'''
     here we will use the viewlog.html to display the contents of the vsearch.log in the form of the html page.
     we will display the contents in the viewlog.html. For this we will render the values of the contents of the
     vsearch.log to the browser


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
    contents=[]
    with open('vsearch.log') as hel:
        for line in hel:
            contents.append([])
            for k in line.split('|'):
                contents[-1].append(escape(k))     # this will add the newest line at the last
    titles=('Form Data','Remote_addr','User_agent','Results')
    return render_template('viewlog.html',the_title='View_Log',the_row_titles=titles,the_data=contents)


if __name__ == '__main__':
    app.run(debug=True)