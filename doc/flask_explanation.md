from flask import Flask

app = Flask(__init__)

@app.route('/')
def index():
return <h1> 'hello world' </h1>
