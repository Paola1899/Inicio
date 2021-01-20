from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
   return render_template("index.html")


'''def square(x):
   return x*x

for i in range(10):
    print("{} squared is {}".format(i, square(i)))'''

