# from flask import Flask, render_template
# app = Flask(__name__)
# # our index route will handle rendering our form
# @app.route('/')
# def index():
#     return render_template("index.html")
# if __name__ == "__main__":
#     app.run(debug=True)
from flask import Flask, render_template, request, redirect # don't forget to import redirect!
app = Flask(__name__)
@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    print(request.form)
    name = request.form['name']
    email = request.form['email']
    return redirect("/show")	# changed this line!
    
# adding this method
@app.route("/show")
def show_user():
    print("Showing the User Info From the Form")
    print(request.form)
    return render_template("index.html")
