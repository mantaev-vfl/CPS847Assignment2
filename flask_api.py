from flask import Flask, jsonify
app = Flask(__name__)
movies = [
    {
        "id": 1,
        "title": "The Joker",
        "releaseDate": "August 31 2019",
        "watched": False
    },
    {
        "id": 2,
        "title": "The Avengers",
        "releaseDate": "May 4 2012",
        "watched": True
    }
]

@app.route('/')
def get_movies():
    return jsonify({'movies': movies})
