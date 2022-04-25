from flask import Flask
from itsdangerous import HMACAlgorithm

from services.home import homeService

app = Flask(__name__)

@app.route("/home")
def home():
    return homeService()



if __name__ == "__main__":
    app.run(port=3000, debug=True)