
from flask import Flask
import requests
app = Flask(__name__)


requests.get("https://www.google.com")

@app.route('/')
def hello_world():
  return 'Hello World!'


@app.route("/bye")
def say_bye():
  return "Bye"

if __name__ == "__main__":
  app.run()
