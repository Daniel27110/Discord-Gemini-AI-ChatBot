from flask import Flask, render_template
from threading import Thread
from waitress import serve

# creates the server
app = Flask("Discord Bot")


# creates the index route
@app.route("/")
def index():
    return "Discord Bot is running!"


# runs the server as a new thread
def run():
    serve(app, host="0.0.0.0", port=8080)


# creates a thread to run the server
def create():
    server = Thread(target=run)
    server.start()
    print("Flask server is running!")
