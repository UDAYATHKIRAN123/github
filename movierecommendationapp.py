from flask import Flask, jsonify, request
import csv

app = Flask(__name__)

all_movies=[]
unliked_movies=[]
liked_movies=[]
notwatched_movies=[]

with open("movies.csv") as f:
    reader=csv.reader(f)
    data=list(reader)
    all_movies=data[1:]

@app.route("/get_movies")

def index():
    return jsonify({
        "data":all_movies[0],
        "message":"sucess"
    })

@app.route("/liked_movies",methods=["POST"])

def likedmovies():
    movie=all_movies[0]
    all_movies=all_movies[1:]
    liked_movies.append(movie)
    return jsonify({
        "message":"sucess"
    })

def unlikedmovies():
    movie=all_movies[0]
    all_movies=all_movies[1:]
    unliked_movies.append(movie)
    return jsonify({
        "message":"sucess"
    })

def notyetwatchedmovies():
    movie=all_movies[0]
    all_movies=all_movies[1:]
    notwatched_movies.append(movie)
    return jsonify({
        "message":"sucess"
    })
