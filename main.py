from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///steps.db'
db = SQLAlchemy(app)

class Steps(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    steps = db.Column(db.Integer)
    date = db.Column(db.String(50))

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        steps = request.form['steps']
        date = request.form['date']
        step_data = Steps(steps=steps, date=date)
        db.session.add(step_data)
        db.session.commit()
        return redirect(url_for('home'))
    all_steps = Steps.query.all()
    return render_template('index.html', steps=all_steps)

@app.route('/clear')
def clear():
    db.session.query(Steps).delete()
    db.session.commit()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
