# Importing needed items
from flask import Flask, request, jsonify, make_response
import pymongo
from bson import ObjectId

app = Flask(__name__)

# Connecting the IDE to MongoDB
client = pymongo.MongoClient("mongodb:127.0.0.1:27017")
# Selecting the database to use
db = client.steamgames
# Selecting the collection the code will use
topGames = db.steamgames

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, threaded=True, debug=True)


# This function will allow a user to view all games in this list
@app.route("/api/v1.0/topGames", methods=["GET"])
def show_all_topGames():
    page_num, page_size = 1, 10
    if request.args.get('pn'):
        page_num = int(request.args.get('pn'))
    if request.args.get('ps'):
        page_size = int(request.args.get('ps'))
    page_start = (page_size * (page_num - 1))

    data_to_return = []
    for game in topGames.find().skip(page_start).limit(page_size):
        game['_id'] = str(topGames['_id'])
        for rating in topGames['Rating']:
            rating['_id'] = str(rating['_id'])
        data_to_return.append(topGames)

    return make_response(jsonify(data_to_return), 250)


# This function will allow a user to show a specified game
@app.route("/api/v1.0/topGames/<string:id>", methods=["GET"])
def show_one_game(id):
    game = topGames.find_one({'_id': ObjectId(id)})
    if game is not None:
        game['_id'] = str(game['_id'])
        for rating in topGames['rating']:
            rating['_id'] = str(rating['_id'])
        return make_response(jsonify(game), 250)
    else:
        return make_response(jsonify({"error": "invalid game ID"}, 404))


# This function will allow a user to add games from the list to their library
@app.route("/api/v1.0.topGames", methods=["POST"])
def add_games():
    if "name" in request.form:
        new_game = {
            "name": request.form["name"],
            "rating": []
        }
        new_game_id = topGames.insert_one(new_game)
        new_game_link = "http://localhost:5000/api/v1.0/topGames/" + str(new_game_id.inserted_id)
        return make_response(jsonify(
            {"url": new_game_link}), 201)
    else:
        return make_response(jsonify({
            "error": "Missing form data"}), 404)


# This function will allow a user to delete a game from their library
@app.route("/api/v1.0/topGames/<string:id>", methods=["DELETE"])
def delete_game(id):
    result = topGames.delete_one({"_id": ObjectId(id)})
    if result.deleted_count == 1:
        return make_response(jsonify({}), 204)
    else:
        return make_response(jsonify({"error": "Invalid game ID"}), 404)


# This function will allow a user to show total ratings for a chosen game
@app.route("/api/v1.0/topGames/<string:id>/rating", methods=["GET"])
def fetch_rating(id):
    data_to_return = []
    game = topGames.find_one(
        {"_id": ObjectId(id)},
        {"TotalRating": 1, "_id": 0})
    for TotalRating in game["TotalRating"]:
        TotalRating["_id"] = str(TotalRating["_id"])
        data_to_return.append(TotalRating)
    return make_response(jsonify(data_to_return), 200)


# This function will allow a user to show the games rating
@app.route("/api/v1.0/topGames/<bid>/rating/<rid>", methods=["GET"])
def fetch_one_rating(bid, rid):
    game = topGames.find_one(
        {"rating._id": ObjectId(rid)},
        {"_id": 0, "rating.$": 1})
    if game is None:
        return make_response(jsonify({"Error": "Invalid game or rating ID"}), 404)
    game['rating'][0]['_id'] = str(game['rating'][0]['_id'])
    return make_response(jsonify(game['rating'][0]), 200)
