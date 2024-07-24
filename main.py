
from flask import Flask, render_template, request
import requests

# Assuming we have sample data for the match and scoreboard
match_info = {
    "match_id": 1,
    "teams": ["Team A", "Team B"],
    "venue": "XYZ Stadium",
    "date": "2023-03-08",
    "time": "14:30"
}

scoreboard = {
    "Team A": {
        "runs": 150,
        "wickets": 3,
        "overs": 20
    },
    "Team B": {
        "runs": 120,
        "wickets": 5,
        "overs": 15
    }
}

app = Flask(__name__)

@app.route("/live_score")
def live_score():
    return render_template("index.html", match_info=match_info, scoreboard=scoreboard)

if __name__ == "__main__":
    app.run(debug=True)
