from flask import Flask

from services.home import homeService

app = Flask(__name__)

@app.route("/home")
def home():
    return homeService()



if __name__ == "__main__":
    app.run(port=6000, debug=True)