from vsearch import search4letters
from flask import Flask, render_template, request, jsonify, escape
from DBcm import UseDatabase

app = Flask(__name__)
app.config['dbconfig'] = {
    'host': '127.0.0.1',
    'user': 'vsearch',
    'password': 'vsearchpasswd',
    'database': 'vsearchlogDB',
    }

def log_request_file(req:'flask_request', res:str) -> None:
    with open('vsearch.log', 'a') as log:
        print(req.form, req.remote_addr, req.user_agent,
            res, file=log, sep='|')

def log_request_db(req:'flask_request', res:str) -> None:
    with UseDatabase(app.config['dbconfig']) as cursor:
        _SQL = ''.join(['insert into log ',
                        '(phrase, letters, ip, browser_string, results) ',
                        'values ',
                        '(%s, %s, %s, %s, %s)'])
        print(_SQL)
        cursor.execute(_SQL, (req.form['phrase'],
                              req.form['letters'],
                              req.remote_addr,
                              req.user_agent.browser,
                              res))

def render_search_response(gen_json:bool=False) -> str:
    """Return either a JSON- or HTML-formatted search response."""
    phrase = request.form['phrase']
    letters = request.form['letters']
    results = str(search4letters(phrase, letters))
    log_request_db(request, results)
    if gen_json:
        return jsonify(the_phrase=phrase,
                       the_letters=letters,
                       the_results=results)
    return render_template('results.html',
                           the_title='Here are your results!',
                           the_phrase=phrase,
                           the_letters=letters,
                           the_results=results)

@app.route('/')						   
@app.route('/entry')
def entry_page() -> 'html':
    """Returns the entry page to browser."""
    return render_template('entry.html',
                           the_title='Welcome to search4letters on the web!',
                           the_url='/search4')

@app.route('/search4', methods=['POST'])
def search4() -> 'html':
    """Returns the results of a call to 'search4letters' to the browser."""
    return render_search_response()

@app.route('/entryjson')
def entry_json_page() -> 'html':
    """Returns the JSON entry page to browser."""
    return render_template('entry.html',
                           the_title='Welcome to search4letters JSON page',
                           the_url='/searchjson')

@app.route('/searchjson', methods=['POST'])
def search4json() -> 'json':
    """Returns the results of a call to 'search4letters' to the browser."""
    return render_search_response(True)

@app.route('/viewlog')
def view_the_log_db() -> 'html':
    with UseDatabase(app.config['dbconfig']) as cursor:
        _SQL = 'select phrase, letters, ip, browser_string, results '+\
            'from log'
        cursor.execute(_SQL)
        context = cursor.fetchall()
    titles = ('Phrase', 'Letters', 'Remote_addr', 'User_agent', 'Results')
    return render_template('viewlog.html',
            the_title = 'View Log', the_row_titles = titles,
			the_data=context)
    
                       
def view_the_log_file() -> 'html':
    contents = []
    with open('vsearch.log') as log:
        for l in log:
            ll = l.strip().split('|')
            contents.append([escape(__) for __ in ll])
    titles = ('Form Data', 'Remote_addr', 'User_agent', 'Results')
    return render_template('viewlog.html',
            the_title = 'View Log', the_row_titles = titles,
			the_data=contents)
	
if __name__ == '__main__':
    app.run(debug=True)

