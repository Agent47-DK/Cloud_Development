from flask import Flask


app = Flask(__name__)

@app.get("/")
@app.get("/hello")
def hello():
    return "Hello Flask App"


if __name__ == "__main__":
    app.run(debug=True)