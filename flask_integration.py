
from flask import Flask, render_template
from flask_restful import Resource, Api, reqparse
import pandas as pd
import functions as db
app = Flask(__name__)
api = Api(app)

# Importing Pandas to create DataFrame

class User(Resource):
    def post(self):
        parser = reqparse.RequestParser()  # initialize

        # Add Arguments
        parser.add_argument('Name', required=True)
        parser.add_argument('Year', required=True)
        args = parser.parse_args()  # parse arguments to dictionary
        # create new dataframe containing new values
        '''for user in args['name'].split:
            if user in list(data['UUID']):
                return {'message': f"'{user}' already exists."}, 401
            else:
                db.init_user_random(args['Name'], args['Year'])
                # read our CSV
                data = pd.read_csv('database.csv')
                return {'data': data.to_dict()}, 200  # return data with 200 OK'''
        name_arg = args["Name"].split()
        print(name_arg)
        print(args)
        db.init_user_random(name_arg, args['Year'])
        # read our CSV
        data = pd.read_csv('database.csv')
        data = data.to_dict()
        return {'data': data}, 220  # return data with 200 OK


    def get(self):
        data = pd.read_csv('database.csv')  # read CSV
        data = data.to_dict()  # convert dataframe to dictionary
        return {'data': data}, 200  # return data and 200 OK code

    pass

class Data(Resource):

    pass


api.add_resource(User, '/user')
api.add_resource(Data, '/data')

if __name__ == "__main__":
    app.run(debug=True)