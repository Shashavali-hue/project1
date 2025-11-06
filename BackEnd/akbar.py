from flask import Flask, request, redirect, url_for, render_template_string
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///names.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the model
class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

# Create the database
with app.app_context():
    db.create_all()

# Home route - asks for name
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        if name:
            new_person = Person(name=name)
            db.session.add(new_person)
            db.session.commit()
            return redirect(url_for('show_names'))

    return render_template_string('''
        <!DOCTYPE html>
        <html>
        <head>
            <title>Enter Name</title>
        </head>
        <body>
            <h2>Enter a Name</h2>
            <form method="POST">
                <input type="text" name="name" placeholder="Enter your name" required>
                <button type="submit">Submit</button>
            </form>
        </body>
        </html>
    ''')

# Show all names
@app.route('/names')
def show_names():
    people = Person.query.all()
    return render_template_string('''
        <!DOCTYPE html>
        <html>
        <head>
            <title>Stored Names</title>
        </head>
        <body>
            <h2>List of Stored Names</h2>
            <table border="1">
                <tr>
                    <th>ID</th>
                    <th>Name</th>
                </tr>
                {% for person in people %}
                <tr>
                    <td>{{ person.id }}</td>
                    <td>{{ person.name }}</td>
                </tr>
                {% endfor %}
            </table>
            <br>
            <a href="{{ url_for('index') }}">Add Another Name</a>
        </body>
        </html>
    ''', people=people)

if __name__ == '__main__':
    app.run(debug=True)
