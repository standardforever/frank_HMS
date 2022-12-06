from hospital import app, db


@app.route("/")
def home():
    return ("Hello frank")
