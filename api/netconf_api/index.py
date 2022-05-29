from flask import Flask

app = Flask(__name__)

@app.route("/configure_interface")
def configure_interface():
  return ''