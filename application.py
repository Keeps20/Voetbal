# export DATABASE_URL=postgres://cfvpvpbzfkdflt:1a4760ff0de0244af65e8b67f87f09bd1f03f23f16e801fd928087f85fe1bdce@ec2-176-34-183-20.eu-west-1.compute.amazonaws.com:5432/d502p688nuugh7

import os
import json
import requests
import csv

from flask import Flask, session, render_template, request, redirect, abort
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

user = []

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

games = {}
id = 0
path = r'C:\Users\gabyh\voetbal\games.csv'
with open(path, 'rt', encoding="utf8") as csv_file:
    reader = csv.reader(csv_file, delimiter=',')
    for row in reader:
        games[id] = {}
        games[id]['datum'] = row[0]
        games[id]['tijd'] = row[1]
        games[id]['wedstrijd'] = (row[2], row[3])
        id += 1
        

@app.route("/")
def index():
    """ Pagina bij het openen van de website """

    return render_template("homepage.html") 

@app.route("/overwinningsfoto")
def overwinningsfoto():
    """ Pagina met alle overwinningsfoto's """

    return render_template("overwinningsfoto.html")

@app.route("/uitslagen")
def uitslagen():
    """ Pagina met de uitslagen van de beker- en competitiewedstrijden """

    return render_template("uitslagen.html") 

@app.route("/spelers")
def spelers():
    """ Pagina met alle spelers """

    return render_template("spelers.html") 

@app.route("/programma")
def programma():
    """ Pagina met het programma voor de wedstrijden die nog gespeeld moeten worden"""
    return render_template("programma.html", game=games)