from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
   return "hola"


'''def square(x):
   return x*x

for i in range(10):
    print("{} squared is {}".format(i, square(i)))'''

