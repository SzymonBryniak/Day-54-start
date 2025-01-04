
from flask import Flask
import requests
app = Flask(__name__)


requests.get("https://www.google.com")

@app.route('/')
def hello_world():
  return 'Hello World!'