# an example for creating a DB with two tables if they do not exist
from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def get_db():
    conn = sqlite3.connect("healthGG.db")
    conn.row_factory = sqlite3.Row  # Enables accessing columns by name
    return conn

def init_db():
    conn = get_db()
    conn.execute("""CREATE TABLE IF NOT EXISTS "doctors" (
	"id"	INTEGER NOT NULL,
	"name"	INTEGER,
	PRIMARY KEY("id" AUTOINCREMENT)
);""")


    
    conn.execute("""CREATE TABLE IF NOT EXISTS "patients" (
	"id"	INTEGER,
	"doctor"	INTEGER,
	"name"	TEXT,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("doctor") REFERENCES "doctors"("id") );""")
    
@app.route("/")
def index():
    conn = get_db()
    patients = conn.execute("SELECT * FROM patients").fetchall()
    conn.close()
    return render_template("index.html", patients=patients)

@app.route("/add", methods=["POST"])
def add_student():
    name = request.form["name"]
    doctor = request.form["doctor"]
    conn = get_db()
    conn.execute("INSERT INTO patients (name, doctor) VALUES (?, ?)", (name, doctor))
    conn.commit()
    conn.close()
    return redirect("/")


if __name__ == "__main__":
    init_db()
    app.run(debug=False, port=8080)

