#!/usr/bin/env python
import flask

import unicorn_hat


# API object
rest_api = flask.Flask(__name__)


@rest_api.route('/set_screen_color')
def set_screen_color():
    """
    API endpoint for '/set_screen_color'
    Valid parameters include 'r' (0-255), 'g' (0-255), 'b' (0-255)
    """
    r = flask.request.args.get('r', default=0, type=int)
    g = flask.request.args.get('g', default=0, type=int)
    b = flask.request.args.get('b', default=0, type=int)
    color = (r, g, b)
    unicorn_hat.set_all(color=color)
    return 'Set screen color to {}'.format(color)


if __name__ == '__main__':
    rest_api.run(host='0.0.0.0')