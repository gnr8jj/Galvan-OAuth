from flask import Flask, redirect, url_for, session, jsonify
from authlib.integrations.flask_client import OAuth

app = Flask(__name__)
app.secret_key = "ebb11308d58ba2587c88cbe1b3dac559eee61f02"

oauth = OAuth(app)




github = oauth.register(
    name='github',
    client_id='Ov23lix9WwMOVJOOKfgM',     
    client_secret='ebb11308d58ba2587c88cbe1b3dac559eee61f02', 
    access_token_url='https://github.com/login/oauth/access_token',
    authorize_url='https://github.com/login/oauth/authorize',
    api_base_url='https://api.github.com/',
    client_kwargs={'scope': 'user:email'},
)




@app.route('/')
def index():
    return '<h2>Flask OAuth Demo</h2><a href="/login">Login with GitHub</a>'


@app.route('/login')
def login():
    redirect_uri = url_for('callback', _external=True)
    return github.authorize_redirect(redirect_uri)


@app.route('/callback')
def callback():
    token = github.authorize_access_token()
    user = github.get('user').json()
    session['user'] = user
    return redirect('/profile')


@app.route('/profile')
def profile():
    if 'user' not in session:
        return "Unauthorized: Please login first.", 401
    
    user = session['user']
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Profile</title>
        <style>
            body {{ font-family: Arial, sans-serif; max-width: 600px; margin: 60px auto; background: #f4f4f4; }}
            .card {{ background: white; border-radius: 12px; padding: 30px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }}
            img {{ border-radius: 50%; width: 100px; height: 100px; }}
            h2 {{ margin: 15px 0 5px; }}
            .info {{ color: #555; margin: 6px 0; }}
            .badge {{ display: inline-block; background: #238636; color: white; padding: 3px 10px; border-radius: 20px; font-size: 13px; }}
            a.logout {{ display: inline-block; margin-top: 20px; color: #c00; text-decoration: none; }}
            a.logout:hover {{ text-decoration: underline; }}
        </style>
    </head>
    <body>
        <div class="card">
            <img src="{user.get('avatar_url', '')}" alt="Avatar">
            <h2>{user.get('name') or user.get('login', 'Unknown')}</h2>
            <span class="badge">@{user.get('login', '')}</span>
            <p class="info">Email: {user.get('email', 'Not public')}</p>
            <a class="logout" href="/logout">Logout</a>
        </div>
    </body>
    </html>
    """


@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/')

@app.route('/api/secure-data')
def secure_data():
    if 'user' not in session:
        return "Unauthorized: Please login first.", 401
    return jsonify({
        "message": "You have access to secure data!",
        "user": session['user'].get('login'),
        "data": {
            "secret": "This is protected information.",
            "level": "confidential"
        }
    })




if __name__ == '__main__':
    app.run(debug=True)