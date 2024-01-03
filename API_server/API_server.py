import jsons
import os
#import ssl

from auth import verify_access_token
from flask import Flask, request

app = Flask(__name__)

#@app.before_request


@app.route('/users', methods = ['GET'])
def get_user():
  # Checks if the access token is present and valid.
  auth_header = request.headers.get('Authorization')
  if 'Bearer' not in auth_header:
    return jsons.dumps({
      'error': 'Access token does not exist.'
    }), 400

  access_token = auth_header[7:]

  #print(auth_header)
  print(access_token)

  if access_token and verify_access_token(access_token):
    users = [
              { 'username': 'Jane Doe', 'email': 'janedoe@example.com'},
              { 'username': 'John Doe', 'email': 'johndoe@example.com'}
            ]
    return jsons.dumps({
              'results': users
            })
  else:
    return jsons.dumps({
      'error': 'Access token is invalid.'
    }), 400

@app.route('/test', methods = ['GET'])
def test():
  return 'Public Access'

if __name__ == '__main__':
  #context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
  #context.load_cert_chain('domain.crt', 'domain.key')
  #app.run(port = 5000, debug = True, ssl_context = context)
  app.run(host='0.0.0.0', debug=True, port='5002', use_reloader=False)
