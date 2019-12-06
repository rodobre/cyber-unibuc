# flask_web/app.py

from flask import Flask,redirect, request,render_template_string
app = Flask(__name__)

@app.route('/')
def home():
  name = request.args.get('name')
  if name == None:
    return redirect("/?name=ninja",code=302)
  return render_template_string('Hello, '+name)


if __name__ == '__main__':
  app.run(debug=False, host='0.0.0.0')
