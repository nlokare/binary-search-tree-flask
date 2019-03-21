from flask import Flask, flash, redirect, request, render_template, g, url_for
import sqlite3 as sqlite
import sys
import os
from os import urandom
from binary_search_tree import BinarySearchTree
app = Flask(__name__)

DATABASE = './data/bst_max_sum.db'

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite.connect(DATABASE)
    db.row_factory = dict_factory
    return db

def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        print('users table created for BST maxSum Database')
        db.commit()

with app.app_context():
    db = get_db()

def get_user(username, password):
    db = sqlite.connect(DATABASE)
    cur = db.cursor()
    cur.execute('SELECT * from users WHERE username = ? AND password = ?', [username, password])
    users = cur.fetchall()
    db.close()
    return users

def check_existing_user(username):
    db = sqlite.connect(DATABASE)
    cur = db.cursor()
    cur.execute('SELECT * from users WHERE username = ?', [username])
    users = cur.fetchall()
    db.close()
    return users

def insert_user(username, password):
    db = sqlite.connect(DATABASE)
    cur = db.cursor()
    cur.execute('INSERT INTO users (username, password) VALUES (?,?)', (username, password))
    db.commit()
    db.close()

def find_max_sum(list_of_vals):
    bst = BinarySearchTree()
    bst.create_from_list(list_of_vals)
    return str(bst.max_sum())

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = get_user(username, password)
        if len(user):
            return redirect(url_for('bst'))
    elif request.method == 'GET':
        return render_template('login.html')

@app.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        error = None
        username = request.form['username']
        password = request.form['password']
        user = check_existing_user(username)
        if len(user):
            error = 'User already exists'
            return render_template('index.html', error=error)
        else:
            insert_user(username, password)
            return render_template('login.html')

@app.route('/bst', methods=['GET'])
def bst():
    return render_template('bst.html')

@app.route('/maxSum', methods=['POST'])
def max_sum():
    vals = request.form['bst_vals']
    max_sum = find_max_sum(vals)
    return render_template('bst.html', max_sum=max_sum, binary_tree_vals=vals)


if __name__ == '__main__':
    if os.environ.get('PORT') is not None:
        app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT'))
    else:
        app.run(debug=True, host='0.0.0.0') 

