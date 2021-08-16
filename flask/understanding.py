# -1
# from flask import Flask
# app=Flask(__name__)
# @app.route("/")
# def hello_world():
#     return "hello world" 
# if __name__=="__main__" :
#     app.run(debug=True)

# -2
# from flask import Flask
# app=Flask(__name__)
# @app.route("/dojo")
# def hello_world():
#     return "dojo" 
# if __name__=="__main__" :
#     app.run(debug=True)

# -3

# from flask import Flask
# app=Flask(__name__)
# @app.route('/<name>')
# def hello_world(name):
#     return "Hi "+ name
# if __name__=="__main__" :
#     app.run(debug=True)

#4

from flask import Flask
app=Flask(__name__)

@app.route('/<int:num>/<name>')
def hello_world(num,name):
    x=""
    for i in range(int(num)):
        x+="<p>"+ name +"</p>"   
    return x
if __name__=="__main__" :
    app.run(debug=True)


