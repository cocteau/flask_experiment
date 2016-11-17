from os import environ
from flask import Flask

app = Flask("botbot")

@app.route("/")
def wakeup():
    return "Hello. I'm Mark's bot!"

port = int(environ.get("PORT", 5000))
app.run(host='0.0.0.0', port=port)
