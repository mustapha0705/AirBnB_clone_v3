from api.v1.views import app_views
from flask import jsonify



@app_views('/status')
def api_status():
    """ Response with the status of an api request."""
    response = {'status': 'OK'}
    return jsonify(response)
