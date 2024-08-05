from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views('/status')
def api_status():
    """ Response with the status of an api request."""
    response = {'status': 'OK'}
    return jsonify(response)


@app_views.route('/stats')
def get_stats():
    """stats of models. """
    stats = {
        'amenities': storage.count('Amenty'),
        'cities': storage.count('City'),
        'places': storage.count('Place'),
        'reviews': storage.count('Review'),
        'states': storage.count('State'),
        'users': storage.count('User')
    }
    return jsonify(stats)
