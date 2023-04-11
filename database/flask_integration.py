
import flask
import simplejson
from flask import Flask
from flask_cors import CORS
from flask_restful import Resource, Api, reqparse
import pandas as pd
from database import functions as db

app = Flask(__name__)
api = Api(app)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
# Importing Pandas to create DataFrame


class RandomUser(Resource):
    def post(self):
        parser = reqparse.RequestParser()  # initialize

        # Add Arguments
        parser.add_argument('Name', required=True)
        parser.add_argument('Year', required=True)
        args = parser.parse_args()  # parse arguments to dictionary
        # create new dataframe containing new values
        data = pd.read_csv("database.csv", index_col=False)
        print(args["Name"])
        name_list = args['Name'].split(' ')
        print(name_list)
        for user in name_list:
            print(user)
            if user in data.Names.values:
                return {'message': f"'{user}' already exists."}, 401

        db.init_user_random(name_list, args['Year'])
        # read our CSV
        data = pd.read_csv('database.csv')
        return {'data': data.to_dict()}, 200  # return data with 200 OK
    pass


class UserData(Resource):
    def post(self):
        parser = reqparse.RequestParser()

        parser.add_argument('uuid', required=True)
        args = parser.parse_args()
        print(args['uuid'])
        data = db.get_userdata(args['uuid'])
        print("checkpoint at line 34")
        data = data.to_dict()
        resp = flask.make_response(simplejson.dumps({'data': data}, ignore_nan=True), 200)
        resp.headers['Access-Control-Allow-Origin'] = '*'
        resp.headers['Access-Control-Allow-Methods'] = 'POST'
        return resp
    pass


api.add_resource(RandomUser, '/randomuser')
api.add_resource(UserData, '/profile')

if __name__ == "__main__":
    app.run(debug=True)
