#!/usr/bin/env python
import flask


# API object
rest_api = flask.Flask(__name__)


@rest_api.route('/api')
def api():
    """
    API endpoint for '/api'
    """
    return 'API endpoints: None'


if __name__ == '__main__':
    rest_api.run(host='0.0.0.0')
    print('*** REST API initialized! ***')