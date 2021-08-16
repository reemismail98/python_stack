from flask import Flask, render_template
app = Flask(__name__)
@app.route('/play')
@app.route('/play/<x>')
@app.route('/play/<x>/<color>')
def index3(x=3,color="blue"):
    return render_template("index.html", times=int(x),color_div=color)

if __name__=="__main__":
    app.run(debug=True)
