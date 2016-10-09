from flask import Flask, render_template, request, redirect, session, flash

from mysqlconnection import MySQLConnector

app = Flask(__name__)
app.secret_key = "secret_key"

mysql = MySQLConnector(app, "sakila")

@app.route("/")
def index():
	query = "SELECT film_id, title FROM film;"
	films = mysql.query_db(query)
	return render_template("index.html", films=films)

@app.route("/film/<film_id>")
def show(film_id):
	query = "SELECT * FROM film WHERE film_id=:film_id"
	data = {"film_id": film_id}

	film = mysql.query_db(query, data)[0]

	query = """SELECT * FROM actor
			LEFT JOIN film_actor ON actor.actor_id=film_actor.actor_id
			WHERE film_actor.film_id=:film_id;"""

	actors = mysql.query_db(query, data)

	return render_template("show.html", film=film, actors=actors)

app.run(debug=True)