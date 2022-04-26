from flask import Flask

from services.home import homeService
from services.fibonacci import fibonacciService

app = Flask(__name__)

@app.route("/home")
def home():
    return homeService()

@app.route("/fibonacci")
def fibonacci():
    fibonacciService(5)
    return {"msg": "fibonacci"}



if __name__ == "__main__":
    app.run(port=3000, debug=True)