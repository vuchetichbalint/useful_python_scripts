from functools import wraps

from flask import Flask, jsonify, request
from flask_restful import Api, Resource, abort

from sklearn.neighbors import KNeighborsClassifier
import pickle

import numpy as np

app = Flask(__name__)
api = Api(app)

api_key = 'secret_key'


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

    #Data cleaning operations
    def preprocess_data(self, x):
        a = np.asarray(x)
        return a  

    def build_model(self, model_params={}):
        self.model = pickle.load(open('mymodel.pkl', 'rb'))
        return

    def apply_model(self, x):
        x = self.preprocess_data(x)
        print(x)
        print(type(x))
        preds = self.model.predict(x)
        return preds.tolist()

    @require_apikey
    def post(self):

        if self.model == None:
            print('elso futas ///////////////////////////////////////////')
            self.build_model()

        message = request.json
        preds = self.apply_model(message['input_features'])
        print(preds)
        return jsonify(predictions=preds)

api.add_resource(PredictorResource, '/predict')

if __name__ == '__main__':
    app.run(debug=True)