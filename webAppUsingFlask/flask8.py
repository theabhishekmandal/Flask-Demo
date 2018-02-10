

'''
- In the preceding examples we were keeping the app.run() method as it is.
  But when we use some other cloud services such as Python Anywhere then it calls the app.run() method on it's own
  and if we try to call the app.run() method on our own then it refuses to launch the code.

- So to avoid this we keep the app.run() inside the main. which allows us to excute it locally and when we
  deploy it to pythonanywhere then it won't get called automatically.
  
- also here we also have created a method called as log_request() which will take to arguments req and res
  req will contain current request object and res will contain the results of the vsearch4letters module.
  Then it will append it to the end of the vsearch.log file
  
- also we are adding a method which will display the viewlogs of the search4letters.py file .But we can see from the 
  vsearch.log file that only the result is being displayed not actually the request object. This is due to that,
  the request object is between <> tags which the browser treats as html tag.

- So as to display the request object we must escape the <> tags .These tags can be replaced by &lt and &gt respectively
   And greatful we are as we have a inbuilt method to do so called as escape, we apply this method on the contents of vsearch.log
'''

from flask import Flask, render_template, request,escape

from webAppUsingFlask.vsearch import search4letters

app=Flask(__name__)


@app.route('/')
@app.route('/entry')
def entry() -> 'html':
    return render_template('entry.html',the_title='Welcome to search for letters on the web')


@app.route('/search4',methods=['POST'])
def do_search() -> str:
    phrase=request.form['phrase']
    letters=request.form['letters']
    title="Here are your results"
    result=str(search4letters(phrase,letters))
    log_request(request,result)
    return render_template('results.html',the_title=title,the_phrase=phrase,the_results=result,the_letters=letters)


def log_request(req:'flask_request',res:str) -> None:
    with open('vsearch.log','a') as log:
        print(req,res,file=log)


@app.route('/viewlog')
def showlog() -> str:
    with open('vsearch.log') as hel:
        contents=hel.read()
    return escape(contents)


if __name__ == '__main__':
    app.run(debug=True)