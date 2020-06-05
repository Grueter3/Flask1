from flask import Flask , render_template, url_for
from forms import RegistrationForm, LoginForm
app =Flask(__name__)

app.config['SECRET_KEY'] = 'c65c7f06871468a784040a9d1d29d247'

posts = [
    {
        'author' : 'J.R.R. Tolkein',
        'title' : 'The Lord of the Rings',
        'content' : 'best story around',
        'date_posted' : 'July 29, 1954 '
    },
    {
        'author' : 'Lao Tzu',
        'title' : 'The Tao Te Ching',
        'content' : 'best wisdom around',
        'date_posted' : '400 B.C ' 
    }
]

@app.route('/register')
def register():
    form = RegistrationForm()
    return render_template('register.html', title ='Register',form = form )

@app.route('/Login')
def Login():
    form = LoginForm()
    return render_template('login.html', title ='Login',form = form )

@app.route('/about')
def about():
    return render_template ('about.html', title = 'About') 

if __name__ == "__main__":
    app.run(debug = True)

