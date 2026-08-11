from flask import Flask, render_template,request,redirect, url_for
from database import create_users_table, add_user, get_user_by_username

create_users_table()
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        database_user = get_user_by_username(username)

        if database_user is None:
            return "Invalid username or password."

        stored_password_hash = database_user[2]
        if password == stored_password_hash:
            return f"Welcome, {username}!"

        return "Invalid username or password."

    return render_template('login.html')

@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        print(f"Registering user: {username} with password: {password}")
        add_user(username, password)
        return redirect(url_for("login"))

    return render_template('register.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
