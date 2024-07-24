## Flask Application Design

### HTML Files

- **index.html**: This will be the main page of the application, displaying the live cricket score updates. It should include the necessary HTML elements to display the scoreboard, such as tables and headings.
- **styles.css**: This file will contain the styling for the application, including the appearance of the scoreboard and any other visual elements on the page.

### Routes

- **"/live_score"**: This route will handle the logic for fetching the live cricket score data from an external API or source. It should use the `requests` library to make the HTTP request and extract the relevant data. The retrieved data should be stored in a format that can be easily displayed on the "index.html" page.

### Example Flask Application Structure

```python
from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/live_score")
def live_score():
    # MAKE API REQUEST TO FETCH LIVE CRICKET SCORE DATA
    response = requests.get("https://api.example.com/cricket/live_score")
    data = response.json()

    # EXTRACT RELEVANT DATA FROM THE API RESPONSE
    match_info = data["match_info"]
    scoreboard = data["scoreboard"]

    # RENDER THE "index.html" PAGE WITH THE FETCHED DATA
    return render_template("index.html", match_info=match_info, scoreboard=scoreboard)

if __name__ == "__main__":
    app.run(debug=True)
```