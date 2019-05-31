# -*- coding: utf-8 -*-

import time 
import sys


from functools import wraps

from flask import Flask, jsonify, request
from flask_restful import Api, Resource, abort

from sklearn.neighbors import KNeighborsClassifier
import pickle

import numpy as np
import pandas as pd

from minio import Minio
import joblib
from io import BytesIO

sys.path.append('/app/src')
#sys.path.insert(0, './src')
from modell import predicting

app = Flask(__name__)
api = Api(app)

api_key = 'secret_key'

minio_client = Minio(
    endpoint='minio:9000',
    access_key='bence',
    secret_key='tollasmadar',
    secure=False
    )


def make_number_if_possible(s):
    if s.replace('.','',1).isdigit():
        if '.' in s:
            return float(s)
        else:
            return int(s)
    return s

def numberify_dict(d):
    for k in d:
        d[k] = make_number_if_possible(d[k])
    return d

def require_apikey(view_function):
    @wraps(view_function)
    # the new, post-decoration function. Note *args and **kwargs here.
    def decorated_function(*args, **kwargs):
        if request.headers.get('token') and request.headers.get('token') == api_key:
            return view_function(*args, **kwargs)
        else:
            abort(401)
    return decorated_function


class PredictorResource(Resource):
    model = None
    header_df = None
    training_data = None

    def predict(self, args):
        d = args.to_dict()
        d = numberify_dict(d)
        df = pd.DataFrame([d])

        x = pd.concat([df, self.header_df])
        x['type'] = 'test'

        with open('/app/shape.txt', 'a') as the_file:
            the_file.write(
                '1:  '+  str( x.shape
                    )
                )
            the_file.write('\n')


        prediction = predicting(x, self.training_data, self.model).iloc[0,:].to_json()

        return prediction

    def apply_model(self, x):
        x = self.preprocess_data(x)
        print(x)
        print(type(x))
        preds = self.model.predict(x)
        return preds.tolist()

    @require_apikey
    def post(self):
        return jsonify(msg='qwe')

        if self.model == None:
            print('elso futas ///////////////////////////////////////////')
            self.build_model()

        if self.header_df == None:
            data = minio_client.get_object('data', 'data_header.df')
            self.header_df = pickle.load(BytesIO(data.data))

        message = request.json
        preds = self.apply_model(message['input_features'])
        print(preds)

        return jsonify(predictions=preds)

    #@require_apikey
    def get(self):
        if self.model == None:
            data = minio_client.get_object('models', 'mymodel.pkl')
            self.model = pickle.load(BytesIO(data.data))

        if self.header_df == None:
            data = minio_client.get_object('data', 'sample_data.csv')
            df = pd.read_csv(BytesIO(data.data))
            self.header_df = df.iloc[0:0]

        if self.training_data == None:
            data = minio_client.get_object('data', 'data_eladasok_2014_2019.csv')
            df = pd.read_csv(BytesIO(data.data))
            df['type'] = 'train'
            self.training_data = df

        prediction = self.predict(request.args)

        return jsonify(prediction=prediction)

api.add_resource(PredictorResource, '/predict')

if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0')