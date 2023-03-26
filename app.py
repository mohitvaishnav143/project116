# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/me")
def home():

    name = "mohit" # write your name
    age = "17" # write your age

    return render_template('index.html' , name = name , age = age)

# define the route to father webpage
@app.route("/father")
def home():

    name = "father" # write your name
    age = "47" # write your age

    return render_template('index.html' , name = name , age = age)


# define the route to mother webpage
@app.route("/mother")
def home():

    name = "mother" # write your name
    age = "43" # write your age

    return render_template('index.html' , name = name , age = age)


# define the route to friends webpage
@app.route("/friends")
def home():

    name = "king" # write your name
    age = "17" # write your age

    return render_template('index.html' , name = name , age = age)






# run the file
if __name__  ==  '__main__':
    app.run(debug=True)
