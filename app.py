from flask import Flask, reuqest
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)



app.run(port=5000, debug=True)