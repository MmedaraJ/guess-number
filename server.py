from flask import Flask, redirect, request, session, render_template
import random
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

@app.route('/')
def show():
    session['message'] = ''
    session['hidden'] = True
    session['colour'] = 'red'
    if 'answer' in session: 
        print(session['answer'])
        if 'guess' in session:
            if int(session['guess']) < session['answer']:
                session['message'] = 'Too Low!'
            elif int(session['guess']) > session['answer']:
                session['message'] = 'Too High!'
            else: 
                session['message'] = f'{session["guess"]} was the number'
                session['colour'] = 'green'
                session['hidden'] = False
    else: session['answer'] = random.randrange(0, 101)
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    session['guess'] = request.form['guess']
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)