from flask import render_template, request, redirect
from app_flask.models.users_models import User
from app_flask import app

@app.route('/')
def index():
    return render_template('register.html')

@app.route('/process/register', methods=['POST'])
def register():
    data = {
        **request.form
    }
    User.create_one(data)
    return redirect('/users')

@app.route('/users')
def users():
    
    users_list = User.obtain_all()
    
    return render_template ('users.html', users_list = users_list)

@app.route('/show/user/<int:id>')
def show(id):

    data = {
        'id' : id
    }

    user = User.obtain_one(data)

    return render_template('show.html', user = user)

@app.route('/edit/user/<int:id>')
def edit(id):
    
    data = {
        'id' : id
    }
    
    user = User.obtain_one(data)
    
    return render_template('edit.html', user = user)

@app.route('/delete/user/<int:id>', methods=['POST'])
def delete_band(id):
    
    data = {
        'id' : id
    }
    
    User.delete_one(data)
    
    return redirect("/users")

@app.route('/update/user/<int:id>', methods=['POST'])
def update_user(id):
    
    data = {
        **request.form,
        'id' : id
    }
    
    User.update_one(data)
    
    return redirect("/users")