#!/usr/bin/env python
import time
import unicornhat


def set_all(color=(255,255,255), brightness=0.2):
    """
    Set all LCDs to green.
    :param color: tuple representing color as (R,G,B)
    :param brightness: max brightness value of pulse (0-1)
    """
    unicornhat.brightness(brightness)
    unicornhat.set_all(color)
    unicornhat.show()


def pulse_all(color=(255,255,255), brightness=0.2, total_time=1, step_time=0.1):
    """
    Set all LCDs to green.
    :param color: tuple representing color as (R,G,B)
    :param brightness: max brightness value of pulse (0-1)
    :param total_time: time for full color pulse to complete, in seconds
    :param step_time: step time between brightness updates, in seconds
    """
    unicornhat.brightness(0) # initial pulse value is 0
    unicornhat.set_all(color)
    unicornhat.show()
    # Calculate pulse data
    steps_half = int(total_time / step_time / 2)
    print('Half steps: {}'.format(steps_half))
    delta_brightness = brightness / steps_half
    # Start pulse
    for _ in range(steps_half): # brighter
        print('Current brightness: {}'.format(unicornhat.get_brightness()))
        brightness = unicornhat.get_brightness() + delta_brightness
        print('New brightness: {} ({} + {})'.format(brightness, unicornhat.get_brightness(), delta_brightness))
        unicornhat.brightness(brightness)
        unicornhat.show()
        time.sleep(step_time)
    for _ in range(steps_half): # darker
        brightness = unicornhat.get_brightness() - delta_brightness
        unicornhat.brightness(brightness)
        unicornhat.show()
        time.sleep(step_time)


if __name__ == '__main__':
    set_all((0,0,0)) # initialize to black