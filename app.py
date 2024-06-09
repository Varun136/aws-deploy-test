from flask import Flask

app = Flask(__name__)

@app.route("/hello")
def hello():
    return {"message":"Hello This is my first app on EC2"}

if __name__ == "__main__":
    app.run()
