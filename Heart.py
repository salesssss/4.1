from flask import Flask, jsonify, request

app = Flask(__name__)

movies = [
    {
        "heart rate": "80bpm",
        "heart_id": ["2011279"],
        "date": ["08/11/2024"]
    },
]


@app.route('/movies', methods=['GET'])
def get_movies():
    return jsonify(movies)


@app.route('/movies', methods=['POST'])
def add_movie():
    movie = request.get_json()
    movies.append(movie)
    return {'message': 'Movie added successfully'}, 201


@app.route('/movies/<string:name>', methods=['DELETE'])
def delete_movie(name):
    global movies
    movies = [movie for movie in movies if movie['name'] != name]
    return {'message': 'Movie deleted successfully'}, 200

@app.route('/movies/<int:index>', methods=['PUT'])
def update_movie(index):
    movies - request.get_json()
    movies[index]=movies
    return jsonify(movies[index]), 200

if __name__ == '__main__':
    app.run(port=5001)