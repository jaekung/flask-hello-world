from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World from Jaekyeong Lee in 3308'

@app.route('/db_test')
def db_test():
    conn = psycopg2.connect("postgresql://jaekung_postgresql_db_user:CkLia5sQ3nvjEvtuTb8zCzpr20H6t606@dpg-csjum5hu0jms73b5irp0-a/jaekung_postgresql_db")
    conn.close()
    return "Database connection successful"


@app.route('/db_create')
def db_create():
    conn = psycopg2.connect("postgresql://jaekung_postgresql_db_user:CkLia5sQ3nvjEvtuTb8zCzpr20H6t606@dpg-csjum5hu0jms73b5irp0-a/jaekung_postgresql_db")
    cur = conn.cursor()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS Basketball(
        First varchar(255),
        Last varchar(255),
        City varchar(255),
        Name varchar(255),
        Number int
        );
    ''')
    conn.commit()
    conn.close()
    return "Basketball table successfully created"


if __name__ == '__main__':
    app.run(debug=True)
