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

@app.route('/db_insert')
def db_insert():
    conn = psycopg2.connect("postgresql://jaekung_postgresql_db_user:CkLia5sQ3nvjEvtuTb8zCzpr20H6t606@dpg-csjum5hu0jms73b5irp0-a/jaekung_postgresql_db")
    cur = conn.cursor()
    cur.execute('''
    INSERT INTO Basketball (First, Last, City, Name, Number)
    Values
    ('Jayson', 'Tatum', 'Boston', 'Celtics', 0),
    ('Stephen', 'Curry', 'San Francisco', 'Warriors', 30),
    ('Nikola', 'Jokic', 'Denver', 'Nuggets', 15),
    ('Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2);
    ''')
    conn.commit()
    conn.close()
    return "Basketball table successfully populated"

@app.route('/db_select')
def db_select():
    conn = psycopg2.connect("postgresql://jaekung_postgresql_db_user:CkLia5sQ3nvjEvtuTb8zCzpr20H6t606@dpg-csjum5hu0jms73b5irp0-a/jaekung_postgresql_db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM Basketball;")
    records = cur.fetchall()
    conn.close()
    
    # Display the query result in HTML format
    response_str = "<table><tr>"
    for row in records:
        for column in row:
            response_str += f"<td>{column}</td>"
        response_str += "</tr>"
    response_str += "</table>"
    
    return response_str

@app.route('/db_drop')
def db_drop():
    conn = psycopg2.connect("postgresql://jaekung_postgresql_db_user:CkLia5sQ3nvjEvtuTb8zCzpr20H6t606@dpg-csjum5hu0jms73b5irp0-a/jaekung_postgresql_db")
    cur = conn.cursor()
    cur.execute("DROP TABLE IF EXISTS Basketball")
    conn.commit()
    conn.close()
    return "Basketball table successfully dropped"