#done by reem  & moath
from flask import Flask, render_template, request, redirect
app = Flask(__name__)
@app.route('/')
def index() :
    return render_template("index.html")

@app.route('/result', methods=['POST'])
def result():
    print("submitted info")
    print(request.form)
    name_from_form = request.form['name']
    location_from_form = request.form['Dojo location']
    language_from_form = request.form['Favorite language']
    Contact_from_form = request.form['Contact via']
    comment_from_form = request.form['Comments']
    
    return render_template("show.html", name_on_template=name_from_form, location_on_template=location_from_form, language_on_template=language_from_form,contact_on_template=Contact_from_form, comments_on_template=comment_from_form)

if __name__ == "__main__":
    app.run(debug=True)


