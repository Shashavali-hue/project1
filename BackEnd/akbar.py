from flask import Flask, request, redirect, render_template_string
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///names.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model
class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

with app.app_context():
    db.create_all()

# Route to take name via URL parameter
@app.route('/')
def home():
    name = request.args.get('name')
    if name:
        new_person = Person(name=name)
        db.session.add(new_person)
        db.session.commit()
        return redirect('/names')

    return render_template_string('''
        <h2>Enter a name</h2>
        <form action="/" method="get">
            <input type="text" name="name" placeholder="Enter your name" required>
            <input type="submit" value="Submit">
        </form>
    ''')

# Route to display stored names
@app.route('/names')
def names():
    people = Person.query.all()
    return render_template_string('''
        <h2>Stored Names</h2>
        <table border="1">
            <tr><th>ID</th><th>Name</th></tr>
            {% for p in people %}
            <tr><td>{{ p.id }}</td><td>{{ p.name }}</td></tr>
            {% endfor %}
        </table>
        <br><a href="/">Add another name</a>
    ''', people=people)

if __name__ == '__main__':
    app.run(debug=True)
