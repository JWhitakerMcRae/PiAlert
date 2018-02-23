#!/usr/bin/env python
import flask

import unicorn_hat


# API object
rest_api = flask.Flask(__name__)


@rest_api.route('/set_screen_color')
def set_screen_color():
    """
    API endpoint for '/set_screen_color'
    Valid parameters include 'r' (0-255), 'g' (0-255), 'b' (0-255), 'brightness' (0-1)
    """
    r = flask.request.args.get('r', default=0, type=int)
    g = flask.request.args.get('g', default=0, type=int)
    b = flask.request.args.get('b', default=0, type=int)
    brightness = flask.request.args.get('brightness', default=0.2, type=float)
    color = (r, g, b)
    unicorn_hat.set_all(color=color, brightness=brightness)
    return 'Set screen color to {}'.format(color)


@rest_api.route('/pulse_screen_color')
def pulse_screen_color():
    """
    API endpoint for '/pulse_screen_color'
    Valid parameters include 'r' (0-255), 'g' (0-255), 'b' (0-255), 'brightness' (0-1), 'total_time' (sec), 'step_time' (sec)
    """
    r = flask.request.args.get('r', default=0, type=int)
    g = flask.request.args.get('g', default=0, type=int)
    b = flask.request.args.get('b', default=0, type=int)
    brightness = flask.request.args.get('brightness', default=0.2, type=float)
    total_time = flask.request.args.get('total_time', default=1, type=float)
    step_time = flask.request.args.get('step_time', default=0.1, type=float)
    color = (r, g, b)
    unicorn_hat.pulse_all(color=color, brightness=brightness, total_time=total_time, step_time=step_time)
    return 'Pulsed screen color of {} (over {} seconds)'.format(color, total_time)


if __name__ == '__main__':
    rest_api.run(host='0.0.0.0') # run flask server