from flask import Flask, request, redirect, render_template
import sqlite3

app = Flask(__name__)

# إنشاء قاعدة البيانات
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
@app.route("/delete/<int:id>", methods=["POST"])
def delete(id):

    connection = sqlite3.connect("bewerbungen.db")
    cursor = connection.cursor()

    cursor.execute("DELETE FROM bewerbungen WHERE id = ?", (id,))

    connection.commit()
    connection.close()

    return redirect("/")
app.run(debug=True)