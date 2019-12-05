#!/usr/bin/python3
from include import *
from routes import api, auth

# ---------------------

print(consts.PROJ_PATH + '../templates')

app = Flask(__name__,
	template_folder= consts.PROJ_PATH + '../templates',
	static_folder= consts.PROJ_PATH + '../static',
	static_url_path= '/static')

# ---------------------

app.register_blueprint(api.api_blueprint)
app.register_blueprint(auth.auth_blueprint)

# ---------------------

@app.route('/')
@app.route('/index')
@app.route('/index.html')
@app.route('/home')
def index():
	return render_template('index.html', title=consts.PAGE_TITLE)

@app.route('/challenges')
@app.route('/tasks')
def challenges():
	return render_template('challenges.html')


@app.route('/register', methods=['GET'])
def register_page():
	return render_template('register.html')
	
@app.route('/login', methods=['GET'])
def login_page():
	return render_template('login.html')

@app.route('/leaderboard', methods=['GET'])
def leaderboard():
	return render_template('leaderboard.html')

@app.route('/news', methods=['GET'])
def news():
	return render_template('news.html')

@app.route('/profile', methods=['GET'])
def profile():
	return render_template('profile.html')

if __name__ == '__main__':
	app.run(host='0.0.0.0')
