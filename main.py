from flask import Flask , render_template #to import the Flask class from the flask module and to import render_template function which is used to render HTML templates

app = Flask(__name__) 
# create a Flask application instance

@app.route("/")  # whenever someone goes to slash route you have to run the below function
def hello_world():
    return render_template("index.html")
    # function to handle requests to the root URL and render the index.html template

app.run(debug=True)  # run the app in debug mode