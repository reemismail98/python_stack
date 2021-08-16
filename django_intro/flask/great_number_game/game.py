from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'
@app.route("/")
def index():
    if 'num' not in session:
        session['num'] = random.randint(1, 100)
    if 'no' in request.form.keys() and request.form['no']:
        if int(request.form['no']) < session['num']:
            session['text']= "Too Low"
        elif int(request.form['no'])>session['num']:
            session['text']= "Too High"
        else:
            session['text']='corrct'
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)



