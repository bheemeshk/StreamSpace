from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World! Bheemesh Here"

@app.route("/user/<username>")
def user(username):
    return "Hello " + username + "!!!!"

if __name__ == "__main__":
    app.run(debug=True)