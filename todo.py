from flask import Flask, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

#find current app path where db is to be stored on os
project_dir = os.path.dirname(os.path.abspath(__file__)) #directory where DB is to be stored

database_file = f'sqlite:///{os.path.join(project_dir, "todo.db")}' #create database file

# Conneccting database_file(todo.db) to SQLAlchemy dependencies
app.config["SQLALCHEMY_DATABASE_URI"] = database_file
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]= False


db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True, nullable=False) 
    todo_item = db.Column(db.String(60), unique=False, nullable =False)

    def __repr__(self):
        return f'Todo({self.todo_item})'

@app.route("/", methods = ['GET', 'POST'])
def index():
    if request.form:
        new_item = request.form.get('')

        todo = Todo(todo_item = new_item)
        db.session.add(todo)
        db.session.commit()
    todos = Todo.query.all()

    return render_template("index.html", todos = todos)


@app.route("/create-todo", methods=["POST"])
def create_todo():
   
    return redirect(url_for("index")) #redirects back to the index page



@app.route('/delete/<todo_item>')
def delete(todo_item):
    todo_data.remove(todo_item)

    return redirect(url_for("index"))


@app.route('/update/<todo_item>', methods=['GET','POST']) #renders page to update
def update(todo_item):

    return render_template('update.html', todo_item = todo_item) # render and take todo_item
    

@app.route('/update_item', methods=['POST'])  #performs the update function
def update_item():
    if request.method == 'POST':
        new_item = request.form.get('new_item')  #get that particular item u just updated from the form


    return redirect(url_for('index')) # redirect to index page


if __name__ == "__main__":
    app.run(debug = True)