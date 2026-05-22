from flask import Flask, request, redirect, render_template
import sqlite3

app = Flask(__name__)


connection = sqlite3.connect("bewerbungen.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS bewerbungen (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    firma TEXT,
    stelle TEXT,
    status TEXT
)
""")

connection.commit()
connection.close()


@app.route("/")
def home():

    connection = sqlite3.connect("bewerbungen.db")
    cursor = connection.cursor()

    cursor.execute("SELECT id, firma, stelle, status FROM bewerbungen")

    daten = cursor.fetchall()

    connection.close()

    return render_template("index.html", daten=daten)

@app.route("/add", methods=["POST"])
def add():

    firma = request.form["firma"]
    stelle = request.form["stelle"]
    status = request.form["status"]

    connection = sqlite3.connect("bewerbungen.db")
    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO bewerbungen (firma, stelle, status) VALUES (?, ?, ?)",
        (firma, stelle, status)
    )

    connection.commit()
    connection.close()

    return redirect("/")

@app.route("/delete/<int:id>", methods=["POST"])
def delete(id):

    connection = sqlite3.connect("bewerbungen.db")
    cursor = connection.cursor()

    cursor.execute("DELETE FROM bewerbungen WHERE id = ?", (id,))

    connection.commit()
    connection.close()

    return redirect("/")
app.run(debug=True)