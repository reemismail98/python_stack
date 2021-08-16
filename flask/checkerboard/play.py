from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index1():
    return render_template("index.html", num_row=8, num_col=8)
@app.route('/<num1>')
def index2(num1):
    return render_template("index.html", num_row=int(num1), num_col=8)
@app.route('/<num1>/<num2>')
def index3(num1,num2):
    return render_template("index.html", num_row=int(num1), num_col=int(num2))
@app.route('/<num1>/<num2>/<color>/<color2>')
def index4(num1,num2,color,color2):
    return render_template("index.html", num_row=int(num1), num_col=int(num2),color_row=color,color_col=color2)    

if __name__=="__main__":
    app.run(debug=True)
