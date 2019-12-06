# flask_web/app.py

from flask import Flask,redirect, request,config
from jinja2 import Template
app = Flask(__name__)

@app.route('/')
def home():
  name = request.args.get('name')
  if name == None:
    return redirect("/?name=ninja",code=302)
  template = Template('Hello, '+name)
  return template.render()

if __name__ == '__main__':
  app.run(debug=False, host='0.0.0.0')
