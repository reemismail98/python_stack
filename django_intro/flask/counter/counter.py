from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'
@app.route("/")
def count():
    session['counter']=0
    return redirect("/count")
@app.route("/count")
def add_counter():
    count=0
    count=session['counter']
    count=count+1
    session['counter']=count
    return render_template("index.html",count=session['counter'])
@app.route("/destroy_session")
def clear():
    return redirect('/')
@app.route("/add_two")
def add():
    session['counter']+=2
    return render_template("index.html",count=session['counter'])

    # @app.route('/result', methods=['POST'])
# def addno():
#     session['counter']=0
#     session['theadd']=0 
#     request.form['number']
#     session['counter']+=int(request.form['number'])
#     session['theadd']+=request.form['number']
#     return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)



