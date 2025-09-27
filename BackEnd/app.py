from flask import Flask,url_for 
app = Flask(__name__)


@app.route('/')
def index():
    profile_url = url_for('show_user_profile', username='dave')
    return f'<a href="{profile_url}">View Dave\'s Profile</a>'

@app.route('/user/<username>')
def show_user_profile(username):
    return f'Profile page for {username}'

if __name__ == "__main__":
    app.run(debug=True)
