import http.client
import json
import requests

api_ip = "http://178.238.217.179:81/predict"
#request_params = ''
request_params = '?a=4&b=kutya'
### api_port = '81'
api_token = 'secret_key'

def get_response_w_post():
    headers = {
        'content-type': "application/json",
        'token': api_token
        }
    body = {'input_features': [[1,2,3,4],[5,6,7,8]] }
    # body = json.dumps({'input_features': [[1,2,3,4],[5,6,7,8]] })
    response = requests.post(api_ip, json=body, headers=headers)
    print(response.json())


def get_response_w_get():
    headers = {
        'content-type': "application/json",
        'token': api_token
        }
    body = {'input_features': [[1,2,3,4],[5,6,7,8]] }
    # body = json.dumps({'input_features': [[1,2,3,4],[5,6,7,8]] })
    print(f'GET to: {api_ip+request_params}')
    response = requests.get(api_ip+request_params, headers=headers)
    print(response.json())





if __name__ == '__main__':
    print(get_response_w_get())
